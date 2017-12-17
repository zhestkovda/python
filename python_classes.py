import  sys

class Organism:
    orgCount = 0
    name = "Organism"
    def __init__(self):
        pass
    def whoIam(self):
        print "I am Organism!"


class Backterium(Organism):
    BackCount = 0
    name = "Backterium"
    def __init__(self):
        pass
    def whoIam(self):
        print "I am Backterium!"


class Animal(Organism):
    name="Animal"
    def __init__(self, name):
        self.name = name
    def whoIam(self):
        print "I am Animal!"
    def displayCount(self):
        print "Total animals %d" % Animal.animalCount
    def displayName(self):
        print "Name : ", self.name

class Flamingo(Animal):
    def __init__(self, name):
        self.name = name
        Organism.orgCount += 1
    def whoIam(self):
        print "I am Flamingo!"

class Lion(Animal):
    def __init__(self, name):
        self.name = name
        Organism.orgCount += 1
    def whoIam(self):
        print "I am Lion!"

class Coliform(Backterium):
    def __init__(self, name):
        self.name = name
        Backterium.BackCount += 1
    def whoIam(self):
        print "I am Coliform!"


def main():
    an1 = Lion("Lion")
    an2 = Flamingo("Flamingo")
    an3 = Coliform("Coliform")
    print Organism.orgCount
    print Backterium.BackCount
    print an1.name
    print an2.name
    print an3.name

if __name__ == "__main__":
    main()
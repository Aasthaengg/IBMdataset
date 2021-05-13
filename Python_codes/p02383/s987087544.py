class Dice:
    def __init__(self, top, south, east, west, north, bottom):
        self.top = top
        self.south = south
        self.east = east
        self.west = west
        self.north = north
        self.bottom = bottom

    def toN(self):
        tmp = self.top
        self.top = self.south
        self.south = self.bottom
        self.bottom = self.north
        self.north = tmp

    def toE(self):
        tmp = self.top
        self.top = self.west
        self.west = self.bottom
        self.bottom = self.east
        self.east = tmp

    def toS(self):
        tmp = self.top
        self.top = self.north
        self.north = self.bottom
        self.bottom = self.south
        self.south = tmp

    def toW(self):
        tmp = self.top
        self.top = self.east
        self.east = self.bottom
        self.bottom = self.west
        self.west = tmp

    def printTop(self):
        print(self.top)


n = input().split()

dice = Dice(int(n[0]), int(n[1]), int(n[2]), int(n[3]), int(n[4]), int(n[5]))

order = input()
for o in order:
    if o == "N":
        dice.toN()
    elif o == "E":
        dice.toE()
    elif o == "S":
        dice.toS()
    elif o == "W":
        dice.toW()

dice.printTop()


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

    def printWest(self):
        print(self.west)

    def printEast(self):
        print(self.east)

    def getTop(self, target):
        if self.top == target:
            return
        for i in range(3):
            self.toN()
            if self.top == target:
                return
        for i in range(3):
            self.toE()
            if self.top == target:
                return

        if self.top != target:
            print("Error")

    def getSouth(self, target):
        if self.south == target:
            return
        for i in range(3):
            self.lotate()
            if self.south == target:
                return
    
    def lotate(self):
        tmp = self.north
        self.north = self.east
        self.east = self.south
        self.south = self.west
        self.west = tmp


n = input().split()
count = int(input())
dice = Dice(int(n[0]), int(n[1]), int(n[2]), int(n[3]), int(n[4]), int(n[5]))

for i in range(count):
    buf = input().split()

    dice.getTop(int(buf[0]))
    dice.getSouth(int(buf[1]))
    dice.printEast()



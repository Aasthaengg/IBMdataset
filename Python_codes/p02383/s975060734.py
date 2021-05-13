class Dice(object):
    def __init__(self, top, south, east, west, north, bottom):
        self.top = top
        self.south = south
        self.east = east
        self.west = west
        self.north = north
        self.bottom = bottom
    def rollN(self):
        prevN = self.north
        prevB = self.bottom
        prevS = self.south
        self.north = self.top
        self.bottom = prevN
        self.south = prevB
        self.top = prevS
    def rollS(self):
        prevS = self.south
        prevB = self.bottom
        prevN = self.north
        self.south = self.top
        self.bottom = prevS
        self.north = prevB
        self.top = prevN
    def rollE(self):
        prevE = self.east
        prevB = self.bottom
        prevW = self.west
        self.east = self.top
        self.bottom = prevE
        self.west = prevB
        self.top = prevW
    def rollW(self):
        prevW = self.west
        prevB = self.bottom
        prevE = self.east
        self.west = self.top
        self.bottom = prevW
        self.east = prevB
        self.top = prevE

diceInit = [int(n) for n in raw_input().split()][:6:]
instruction = raw_input()

diceI = Dice(diceInit[0], diceInit[1], diceInit[2], diceInit[3], diceInit[4], diceInit[5])

for item in instruction:
    if item == 'N':
        diceI.rollN()
    elif item == 'E':
        diceI.rollE()
    elif item == 'W':
        diceI.rollW()
    elif item == 'S':
        diceI.rollS()

print diceI.top
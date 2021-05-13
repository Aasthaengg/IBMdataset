class Dice:
    def __init__(self,pips):
        self.top = pips[0]
        self.south = pips[1]
        self.east = pips[2]
        self.west = pips[3]
        self.north =pips[4]
        self.bottom=pips[5]
    def show_top(self):
        print(self.top)
    def n(self):
        tmp = self.top
        self.top = self.south
        self.south = self.bottom
        self.bottom = self.north
        self.north = tmp
    def s(self):
        tmp = self.top
        self.top = self.north
        self.north = self.bottom
        self.bottom = self.south
        self.south = tmp
    def e(self):
        tmp = self.top
        self.top = self.west
        self.west = self.bottom
        self.bottom = self.east
        self.east = tmp
    def w(self):
        tmp = self.top
        self.top = self.east
        self.east = self.bottom
        self.bottom = self.west
        self.west = tmp

pips = [int(x) for x in input().split()]
dice = Dice(pips)
move = input()
for m in move:
    if m == "N":
        dice.n()
    if m == "S":
        dice.s()
    if m == "E":
        dice.e()
    if m == "W":
        dice.w()

dice.show_top()
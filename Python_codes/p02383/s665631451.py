class Dice:
    def __init__(self):
        self.top = 1
        self.dside = 2
        self.rside = 3
        self.lside = 4
        self.uside = 5
        self.bottom = 6
    def north(self):
        (self.top, self.dside, self.bottom, self.uside) = (self.dside, 
            self.bottom, self.uside, self.top)
    def east(self):
        (self.top, self.lside, self.bottom, self.rside) = (self.lside,
            self.bottom, self.rside, self.top)
    def south(self):
        (self.top, self.dside, self.bottom, self.uside) = (self.uside, 
            self.top, self.dside, self.bottom)
    def west(self):
        (self.top, self.lside, self.bottom, self.rside) = (self.rside,
            self.top, self.lside, self.bottom)

num, dice = list(map(int, input().split())), Dice()
label = {i+1:num[i] for i in range(6)}
com = [i for i in input()]
for i in com:
    if i=="N":
        dice.north()
    elif i=="E":
        dice.east()
    elif i=="S":
        dice.south()
    else:
        dice.west()
print(label[dice.top])


class Dice():

    def __init__(self, d):
        self.d = d
        self.north = [2, 6, 3, 4, 1, 5]
        self.south = [5, 1, 3, 4, 6, 2]
        self.east = [4, 2, 1, 6, 5, 3]
        self.west = [3, 2, 6, 1, 5, 4]
        self.label = {(d[0], d[1]): d[2]}

    def roll(self, direction):
        if direction == 'S':
            self.d = [ self.d[self.south[i]-1] for i in range(6) ]
        elif direction == 'N':
            self.d = [ self.d[self.north[i]-1] for i in range(6) ]
        elif direction == 'E':
            self.d = [ self.d[self.east[i]-1] for i in range(6) ]
        elif direction == 'W':
            self.d = [ self.d[self.west[i]-1] for i in range(6) ]

    def rollAll(self):
        for i in range(4):
            for i in range(4):
                self.roll('E')
                self.label[(self.d[0], self.d[1])] = self.d[2]
            self.roll('S')
        self.roll('E')
        self.roll('S')
        for i in range(4):
            self.roll('E')
            self.label[(self.d[0], self.d[1])] = self.d[2]
        self.roll('S')
        self.roll('S')
        for i in range(4):
            self.roll('E')
            self.label[(self.d[0], self.d[1])] = self.d[2]

    def getLabel(self):
        return self.label

    def getDice(self):
        return self.d

s = [ int(s) for s in input().split() ]
n = int(input())
dice = Dice(s)
dice.rollAll()
l = dice.getLabel()

for i in range(n):
    a,b = [ int(s) for s in input().split() ]
    print(l[(a,b)])


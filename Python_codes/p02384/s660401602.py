class Dice:
    def __init__(self, data):
        self.data = data
    
    def move(self, direction):
        if direction == 'E':
            self.data[0], self.data[3], self.data[5], self.data[2] = \
                self.data[3], self.data[5], self.data[2], self.data[0]
        elif direction == 'N':
            self.data[0], self.data[4], self.data[5], self.data[1] = \
                self.data[1], self.data[0], self.data[4], self.data[5]
        elif direction == 'S':
            self.data[0], self.data[1], self.data[5], self.data[4] = \
                self.data[4], self.data[0], self.data[1], self.data[5]
        elif direction == 'W':
            self.data[0], self.data[2], self.data[5], self.data[3] = \
                self.data[2], self.data[5], self.data[3], self.data[0]
        elif direction == 'R':
            self.data[1], self.data[2], self.data[4], self.data[3] = \
                self.data[3], self.data[1], self.data[2], self.data[4]
        elif direction == 'L':
            self.data[1], self.data[2], self.data[4], self.data[3] = \
                self.data[2], self.data[4], self.data[3], self.data[1]

    def moveTopTo(self, target):
        for a in range(4):
            if self.data[0] == target:
                break
            self.move('W')
        if self.data[4] == target:
            self.move('S')
        elif self.data[1] == target:
            self.move('N')
    
    def moveFrontTo(self, target):
        for a in range(4):
            if self.data[1] == target:
                break
            self.move('R')

    def getTop(self):
        return self.data[0]
    
    def getRight(self):
        return self.data[2]

dice = Dice(input().split())
c = int(input())

for a in range(c):
    (t, f) = input().split()
    dice.moveTopTo(t)
    dice.moveFrontTo(f)
    print(dice.getRight())
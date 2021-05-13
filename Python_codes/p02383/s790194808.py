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

    def getTop(self):
        return self.data[0]

dice = Dice(input().split())
cmd = input()
for i in range(len(cmd)):
    dice.move(cmd[i])
print(dice.getTop())
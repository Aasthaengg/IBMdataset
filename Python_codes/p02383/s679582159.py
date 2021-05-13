class Dice:
    def __init__(self, dice):
        self.dice = dice
        self.buff = [n for n in dice]
    def east(self):
        self.dice[0] = self.buff[3]
        self.dice[2] = self.buff[0]
        self.dice[5] = self.buff[2]
        self.dice[3] = self.buff[5]
        self.buff = [n for n in self.dice]
    def west(self):
        self.dice[0] = self.buff[2]
        self.dice[2] = self.buff[5]
        self.dice[5] = self.buff[3]
        self.dice[3] = self.buff[0]
        self.buff = [n for n in self.dice]
    def north(self):
        self.dice[0] = self.buff[1]
        self.dice[1] = self.buff[5]
        self.dice[5] = self.buff[4]
        self.dice[4] = self.buff[0]
        self.buff = [n for n in self.dice]
    def south(self):
        self.dice[0] = self.buff[4]
        self.dice[1] = self.buff[0]
        self.dice[5] = self.buff[1]
        self.dice[4] = self.buff[5]
        self.buff = [n for n in self.dice]

nums = list(map(int, input().split()))
d = Dice(nums)
way = input()

for w in way:
    if w == "E":
        d.east()
    if w == "W":
        d.west()
    if w == "N":
        d.north()
    if w == "S":
        d.south()

print(d.dice[0])


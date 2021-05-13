class Dice(object):
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6
    def east(self):
        prev_s6 = self.s6
        self.s6 = self.s3
        self.s3 = self.s1
        self.s1 = self.s4
        self.s4 = prev_s6
    def west(self):
        prev_s6 = self.s6
        self.s6 = self.s4
        self.s4 = self.s1
        self.s1 = self.s3
        self.s3 = prev_s6
    def north(self):
        prev_s6 = self.s6
        self.s6 = self.s5
        self.s5 = self.s1
        self.s1 = self.s2
        self.s2 = prev_s6
    def south(self):
        prev_s6 = self.s6
        self.s6 = self.s2
        self.s2 = self.s1
        self.s1 = self.s5
        self.s5 = prev_s6
    def top(self):
        return self.s1

s1, s2, s3, s4, s5, s6 = map(int, input().split())
dice = Dice(s1, s2, s3, s4, s5, s6)
order = input()
for c in order:
    if c == 'N':
        dice.north()
    elif c == 'W':
        dice.west()
    elif c == 'E':
        dice.east()
    elif c == 'S':
        dice.south()
print(dice.top())
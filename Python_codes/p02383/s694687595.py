class Dice:
    """サイコロを操作するクラス"""
    def __init__(self, num):
        self.num = num
    def roll_north(self):
        tmp = self.num[:]
        self.num[0] = tmp[1]
        self.num[1] = tmp[5]
        self.num[4] = tmp[0]
        self.num[5] = tmp[4]
    def roll_south(self):
        tmp = self.num[:]
        self.num[0] = tmp[4]
        self.num[1] = tmp[0]
        self.num[4] = tmp[5]
        self.num[5] = tmp[1]
    def roll_east(self):
        tmp = self.num[:]
        self.num[0] = tmp[3]
        self.num[2] = tmp[0]
        self.num[3] = tmp[5]
        self.num[5] = tmp[2]
    def roll_west(self):
        tmp = self.num[:]
        self.num[0] = tmp[2]
        self.num[2] = tmp[5]
        self.num[3] = tmp[0]
        self.num[5] = tmp[3]
    def print_dice(self):
        print(self.num)
    def print_top(self):
        print(self.num[0])

num = list(map(int, input().split()))
dice = Dice(num)
for i in input():
    if i == "N":
        dice.roll_north()
    elif i == "S":
        dice.roll_south()
    elif i == "E":
        dice.roll_east()
    elif i == "W":
        dice.roll_west()
    else:
        print("input error")
dice.print_top()


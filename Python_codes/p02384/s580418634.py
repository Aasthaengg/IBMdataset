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
    def roll_right(self):
        tmp = self.num[:]
        self.num[1] = tmp[3]
        self.num[2] = tmp[1]
        self.num[3] = tmp[4]
        self.num[4] = tmp[2]
    def print_dice(self):
        print(self.num)
    def print_top(self):
        print(self.num[0])

num = list(map(int, input().split()))
dice = Dice(num)
for i in range(int(input())):
    top, front = map(int, input().split())
    while not(top == dice.num[0] or front == dice.num[1]):
        dice.roll_north()
    while top != dice.num[0]:
        dice.roll_east()
    while front != dice.num[1]:
        dice.roll_right()
    print(dice.num[2])

# -*- coding: utf-8 -*-


class Dice:
    def __init__(self, n):
        self.upper    = n[0]
        self.backward = n[1]
        self.right    = n[2]
        self.left     = n[3]
        self.ahead    = n[4]
        self.bottom   = n[5]

    def roll_north(self):
        self.upper, self.ahead, self.bottom, self.backward = self.backward, self.upper, self.ahead, self.bottom

    def roll_south(self):
        self.upper, self.ahead, self.bottom, self.backward = self.ahead, self.bottom, self.backward, self.upper

    def roll_east(self):
        self.upper, self.right, self.bottom, self.left = self.left, self.upper, self.right, self.bottom

    def roll_west(self):
        self.upper, self.right, self.bottom, self.left = self.right, self.bottom, self.left, self.upper

    def roll_side(self):
        self.ahead, self.right, self.backward, self.left = self.left, self.ahead, self.right, self.backward


dice_info = Dice(list(map(int, input().split())))
q = int(input())

for i in range(q):
    upper, ahead = map(int, input().split())

    if upper is dice_info.left:
        dice_info.roll_east()
        
    elif upper is dice_info.right:
        dice_info.roll_west()

    while not (upper == dice_info.upper or ahead == dice_info.ahead):
        dice_info.roll_north()

    while upper != dice_info.upper:
        dice_info.roll_east()

    while ahead != dice_info.ahead:
        dice_info.roll_side()

    print(dice_info.left)

# サイコロ        初期状態
#    [1]           N
# [4][2][3][5]   W[1]E
#    [6]           S
#
# 上記の順番でラベルに対する整数が与えられる
# l1 l2 l3 l4 l5 l6
# {N, E, W, S} ...
import sys

class Dice:
    def __init__(self, l1, l2, l3, l4, l5, l6):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.l4 = l4
        self.l5 = l5
        self.l6 = l6
        self.tmp = 0
    def move_n(self):
        self.tmp = self.l5
        self.l5 = self.l1
        self.l1 = self.l2
        self.l2 = self.l6
        self.l6 = self.tmp
    def move_s(self):
        self.tmp = self.l2
        self.l2 = self.l1
        self.l1 = self.l5
        self.l5 = self.l6
        self.l6 = self.tmp
    def move_e(self):
        self.tmp = self.l3
        self.l3 = self.l1
        self.l1 = self.l4
        self.l4 = self.l6
        self.l6 = self.tmp
    def move_w(self):
        self.tmp = self.l4
        self.l4 = self.l1
        self.l1 = self.l3
        self.l3 = self.l6
        self.l6 = self.tmp

d1 = Dice(*map(int, input().split()))

for line in sys.stdin:
    for s in list(line):
        if s == 'N':
            d1.move_n()
        elif s == 'S':
            d1.move_s()
        elif s == 'E':
            d1.move_e()
        elif s == 'W':
            d1.move_w()
print(d1.l1)

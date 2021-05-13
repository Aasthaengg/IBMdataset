# サイコロ        初期状態
#    [1]           N
# [4][2][3][5]   W[1]E
#    [6]           S
#
# 上記の順番でラベルに対する整数が与えられる
# l1 l2 l3 l4 l5 l6
# 「上面[1] 前面[2]」が与えられて右側の面[3]を答える

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
    def show(self):
        return self.l1, self.l2, self.l3, self.l4, self.l5, self.l6

d1 = Dice(*map(int, input().split()))
n = int(input())

for _ in range(n):
    ue, mae = map(int, input().split())
    ne_switch = 0
    while d1.l2 != mae:
        if ne_switch < 3:
            d1.move_n()
            ne_switch+=1
        elif 3 <= ne_switch :
            d1.move_e()
            ne_switch+=1
        if ne_switch == 6: ne_switch = 0
    while d1.l1 != ue:
        d1.move_e()
    print(d1.l3)

#coding:utf-8
#1_11_A 2015.4.17
class Dice:
    def __init__(self,ary):
        self.top = ary[0]
        self.south = ary[1]
        self.east = ary[2]
        self.west = ary[3]
        self.north = ary[4]
        self.bottom = ary[5]

    def get_top(self):
        return self.top

    def roll_n(self):
        self.top , self.south , self.bottom , self.north = self.south , self.bottom , self.north , self.top

    def roll_s(self):
        self.top , self.north , self.bottom , self.south = self.north , self.bottom , self.south , self.top

    def roll_e(self):
        self.top , self.west , self.bottom , self.east = self.west , self.bottom , self.east , self.top

    def roll_w(self):
        self.top , self.east , self.bottom , self.west = self.east , self.bottom , self.west , self.top

dice = Dice(input().split())
cmds = input()
for cmd in cmds:
    if cmd == 'N':
        dice.roll_n()
    elif cmd == 'S':
        dice.roll_s()
    elif cmd == 'E':
        dice.roll_e()
    elif cmd == 'W':
        dice.roll_w()

print(dice.get_top())
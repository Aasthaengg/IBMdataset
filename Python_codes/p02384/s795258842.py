#coding:utf-8
#1_11_B 2015.4.20
class Dice:
    def __init__(self,ary):
        self.top , self.south , self.east , self.west , self.north ,self.bottom = ary

    def roll_n(self):
        self.top , self.south , self.bottom , self.north = self.south , self.bottom , self.north , self.top

    def roll_e(self):
        self.top , self.west , self.bottom , self.east = self.west , self.bottom , self.east , self.top

    def twist(self):
        self.north , self.west , self.south , self.east = self.east , self.north , self.west , self.south

dice = Dice(input().split())
for i in range(int(input())):
    top,south = input().split()
    while dice.top != top or dice.south != south:
        if dice.top == top:
            while dice.south != south:
                dice.twist()
        elif dice.south == south:
            while dice.top != top:
                dice.roll_e()
        else:
            dice.roll_n()
    print(dice.east)
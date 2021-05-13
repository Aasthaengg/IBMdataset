#!/usr/bin/env python3
# coding: utf-8

class dice ():
    def __init__(self, data):
        self.up = data[0]
        self.down = data[5]
        self.left = data[3]
        self.right =data[2]
        self.front = data[1]
        self.back = data[4]

    def turn_s(self):
        tmp = self.up
        self.up = self.back
        self.back = self.down
        self.down = self.front
        self.front = tmp

    def turn_n(self):
        tmp = self.up
        self.up = self.front
        self.front = self.down
        self.down = self.back
        self.back = tmp

    def turn_w(self):
        tmp = self.up
        self.up = self.right
        self.right = self.down
        self.down = self.left
        self.left = tmp

    def turn_e(self):
        tmp = self.up
        self.up = self.left
        self.left = self.down
        self.down = self.right
        self.right = tmp

    def turn(self, rotate="N"):
        if (rotate == "N"):
            self.turn_n()
        elif (rotate == "E"):
            self.turn_e()
        elif (rotate == "W"):
            self.turn_w()
        elif (rotate == "S"):
            self.turn_s()
        else:
            none

    def get_up(self):
        return self.up



dicedata = input().split()
orderdata = input()

newdice = dice(dicedata)

[newdice.turn(orderdata[idx]) for idx in range(0, len(orderdata))]

print(newdice.get_up())


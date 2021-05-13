#!/usr/bin/env python

class Dice:
    def __init__(self, top, s, e, w, n, bottom):
        self.top    = top
        self.s      = s
        self.e      = e
        self.w      = w
        self.n      = n
        self.bottom = bottom

    def rotate(self, dist):
        if dist == 'N':
            self.top, self.s, self.n, self.bottom = self.s, self.bottom, self.top, self.n 
        elif dist == 'S':
            self.s, self.bottom, self.top, self.n = self.top, self.s, self.n, self.bottom 
        elif dist == 'E':
            self.top, self.e, self.w, self.bottom = self.w, self.top, self.bottom, self.e 
        elif dist == 'W':
            self.w, self.top, self.bottom, self.e = self.top, self.e, self.w, self.bottom 

if __name__ == '__main__':
    num = map(int, raw_input().split())
    dice = Dice(*num)

    for c in raw_input():
        dice.rotate(c)
    print dice.top



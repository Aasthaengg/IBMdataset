#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
???????????? I

?¬?????±??????????????????????????????????????????¢??????????????\??¬????????§????????????????????°????????????????????????????????????
   +--+
 ???|???|
+--+--+--+--+
|???|???|???|???|
+--+--+--+--+
 ???|???|
   +--+

"""

class Dice:
    T = 0
    S = 1
    E = 2
    W = 3
    N = 4
    B = 5

    """ ????????????????????? """
    def __init__(self): # ?????????????????????
        self.side = [1, 2, 3, 4, 5, 6]
        self.top = 0

    def setDice(self, arr):  # ??¢??????????????????
        self.side = arr[0:6]

    def Turn(self, dir): # ?????????????????¢??????
        s = self.side

        if dir == "N":     # ????????¢??????
            #    Top 0     South 1   East 2    West 3    North 4   Bottom 5
            t = [s[Dice.S],s[Dice.B],s[Dice.E],s[Dice.W],s[Dice.T],s[Dice.N]]
        elif dir == "S": # ????????¢??????
            t = [s[Dice.N],s[Dice.T],s[Dice.E],s[Dice.W],s[Dice.B],s[Dice.S]]
        elif dir == "E": # ??±?????¢??????
            t = [s[Dice.W],s[Dice.S],s[Dice.T],s[Dice.B],s[Dice.N],s[Dice.E]]
        elif dir == "W": # ?\??????¢??????
            t = [s[Dice.E],s[Dice.S],s[Dice.B],s[Dice.T],s[Dice.N],s[Dice.W]]
        elif dir == "L": # ???????????¢
            t = [s[Dice.T],s[Dice.W],s[Dice.S],s[Dice.N],s[Dice.E],s[Dice.B]]
        elif dir == "R": # ???????????¢
            t = [s[Dice.T],s[Dice.E],s[Dice.N],s[Dice.S],s[Dice.W],s[Dice.B]]

        self.side = t
#        print("{0} T0:{1} S1:{2} W2:{3} E3:{4} N4:{5} B5:{6} ".format(dir, self.side[0],self.side[1], self.side[2],self.side[3], self.side[4],self.side[5]))

    def Search(self, tval, sval, dir): # ?????¢??¨?????¢???????????????????????????????????¢???????????????
    
        if self.side[Dice.E] == tval:
            self.Turn("W")
        elif self.side[Dice.W] == tval:
            self.Turn("E")
        elif self.side[Dice.N] == tval:
            self.Turn("S")
        elif self.side[Dice.S] == tval:
            self.Turn("N")
        elif self.side[Dice.B] == tval:
            self.Turn("N")
            self.Turn("N")

        for i in range(3): # ?????¢?????????????????????????????§????????????
            if self.side[Dice.S] == sval:
                break
            self.Turn("L")
            
        return self.side[dir]

dnum = list(map(int,input().strip().split()))
d = Dice()
d.setDice(dnum)
cnum = int(input().strip())
for c in range(cnum):
    cmd = list(map(int,input().strip().split()))
    val = d.Search(cmd[0], cmd[1], Dice.E)
    print(val)
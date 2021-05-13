# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 15:20:49 2020

@author: liang
"""

N, Y = map(int, input().split())
y = Y //1000

a = 0
while a <= N and y - 10*a >=0:
    bt = y - N - 9*a
    ct = 5*N - y + 5*a
    if bt < 0 or ct < 0:
        a += 1
        continue
    if bt % 4 == 0 and ct % 4 == 0:
        b = bt//4
        c = ct//4
        print(a,b,c)
        break
    a += 1
else:
    print(-1,-1,-1)
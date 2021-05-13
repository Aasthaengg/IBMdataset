# -*- coding: utf-8 -*-
n = input()
a = [int(s) for s in input().split()]
r = 0

def checkNum(l, c):
    for i in l:
        if (i % 2 != 0):
            return c

    c += 1
    return checkNum([j / 2 for j in l], c)

print(checkNum(a, r))
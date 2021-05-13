# -*- coding: utf-8 -*-
import sys
from collections import defaultdict, deque
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline()[:-1]


def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    w = set()
    c = 0
    for e in a:
        if 1 <= e <= 399:
            w.add(1)
        elif 400 <= e <= 799:
            w.add(2)
        elif 800 <= e <= 1199:
            w.add(3)
        elif 1200 <= e <= 1599:
            w.add(4)
        elif 1600 <= e <= 1999:
            w.add(5)
        elif 2000 <= e <= 2399:
            w.add(6)
        elif 2400 <= e <= 2799:
            w.add(7)
        elif 2800 <= e <= 3199:
            w.add(8)
        elif 3200 <= e:
            c += 1
    print(max(1, len(w)), len(w) + c)


t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()

"""

"""


# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():

    w, h, n = [int(x) for x in input().split()]
    l, r, u, d = 0, w, h, 0
    for _ in range(n):
        x, y, a = [int(x) for x in input().split()]
        if a == 1:
            l = max(l, x)
        elif a == 2:
            r = min(r, x)
        elif a == 3:
            d = max(d, y)
        else:
            u = min(u, y)
    print(max(0, (r - l)) * max(0, (u - d)))

    
    

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

2 3 4 4
3 4 4
2 3 4
2 3 4
2 4 4


"""

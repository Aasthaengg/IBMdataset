# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    c = []
    ok = 1
    for i in range(3):
        c.append([int(x) for x in input().split()])
        if i:
            if c[i] != c[i-1]:
                d = c[i][0] - c[i-1][0]
                c[i] = [x - d for x in c[i]]
            if c[i] != c[i-1]:
                ok = 0
    if ok:
        print("Yes")
    else:
        print("No")
    

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

1 + k



"""

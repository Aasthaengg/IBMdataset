# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    d = defaultdict(int)
    for e in a:
        d[e] += 1
    sm = 0
    xd = defaultdict(int)
    for k in d:
        if d[k] >= 2:
            xd[k] = (d[k] * (d[k] - 1)) // 2
        sm += xd[k]
    for e in a:
        d[e] -= 1
        sm -= xd[e]
        x = 0
        if d[e] >= 2:
            x = (d[e] * (d[e] - 1)) // 2
        print(sm + x)
        sm += xd[e]
        d[e] += 1


    

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""


"""

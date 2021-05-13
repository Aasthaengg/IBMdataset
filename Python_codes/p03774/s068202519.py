# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    n, m = [int(x) for x in input().split()]
    s = []
    for _ in range(n):
        s.append([int(x) for x in input().split()])
    c = []
    for _ in range(m):
        c.append([int(x) for x in input().split()])
    for x, y in  s:
        ans = 0
        d = float('inf')
        for i, (a, b) in enumerate(c):
            if abs(x-a) + abs(y-b) < d:
                ans = i
                d = abs(x-a) + abs(y-b)
        print(ans + 1)
        

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""


"""

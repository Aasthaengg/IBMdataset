# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    n = int(input())
    r = []
    for i in range(n):
        s, x = [x for x in input().split()]
        r.append((s, - int(x), i + 1))
    r.sort()
    for e in r:
        print(e[2])

    



t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

"""

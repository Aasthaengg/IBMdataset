# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    s = input()
    chars = set([x for x in s])
    mn = len(s)
    for c in chars:
        mx = max([len(x) for x in s.split(c)])
        mn = min(mn, mx)
    print(mn)
    



t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""



"""

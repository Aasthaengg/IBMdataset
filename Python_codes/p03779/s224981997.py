# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    n = int(input())
    pos = 0
    i = 0
    while pos < n:
        i += 1
        pos += i
    print(min(n, i))

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

abc

"""

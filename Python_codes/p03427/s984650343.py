# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    s = [x for x in input()]
    n = int(''.join(s))
    k = len(s)
    a = s[0] + '9' * (k - 1)
    b = int(a)
    a = [int(x) for x in a]
    if b > n:
        a[0] -= 1
    print(sum(a))


t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""


"""

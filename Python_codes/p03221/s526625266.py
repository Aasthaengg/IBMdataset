# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd, ceil, atan, pi
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')
import string
# string.ascii_lowercase
from bisect import bisect_left
MOD = int(1e9)+7
INF = float('inf')


def solve():
    # n, m = [int(x) for x in input().split()]
    n, m = [int(x) for x in input().split()]
    ans = [0] * m
    a = defaultdict(list)
    for i in range(m):
        p, y = [int(x) for x in input().split()]
        a[p].append((y, i))

    for p in a:
        r = a[p]
        r.sort()
        for x, (y, i) in enumerate(r):
            ans[i] = f'{p:06}{x+1:06}'
    for r in ans:
        print(r)

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""
a b a
d c d
a b a
"""

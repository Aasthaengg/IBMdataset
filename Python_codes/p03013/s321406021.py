# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd, ceil
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')
import string
# string.ascii_lowercase
from bisect import bisect_left
MOD = int(1e9)+7
INF = float('inf')


def solve():
    n, m = [int(x) for x in input().split()]
    d = [0] * (n+1)
    d[0] = 1
    for _ in range(m):
        x = int(input())
        d[x] = -1

    for i in range(1, n+1):
        if d[i] != -1:
            if d[i-1] != -1:
                d[i] = d[i-1]
            if i > 1 and d[i-2] != -1:
                d[i] += d[i-2]
            d[i] %= MOD

    print(d[n]%MOD)

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

azyxwvutsrqponmlkjihgfedcb

"""

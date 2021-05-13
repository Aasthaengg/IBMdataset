# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd, ceil, atan, pi
def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')
import string
# string.ascii_lowercase
from bisect import bisect_left, bisect_right
from functools import lru_cache, reduce
MOD = int(1e9)+7
INF = float('inf')


def solve():
    n = int(input())
    s = input()
    p = [0] * n
    r = [0] * n
    for i in range(n):
        if i: p[i] += p[i-1]
        if s[i] == '#': p[i] += 1
    for i in range(n-1,-1,-1):
        if i+1<n: r[i] += r[i+1]
        if s[i] == '.': r[i] += 1
    ans = min(p[-1], r[0])
    for i in range(n-1):
        ans = min(ans, p[i] + r[i + 1])
    print(ans)
    

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""
1
4
-1 1 1 -1

"""

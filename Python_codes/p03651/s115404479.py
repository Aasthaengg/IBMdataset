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
    # n = int(input())
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    g = reduce(gcd, a)

    m = max(a)
    if k <= m and k % g == 0:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""
1
4
-1 1 1 -1

"""

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
from functools import lru_cache
MOD = int(1e9)+7
INF = float('inf')


def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    
    s = sum(a)
    x = s - 2 * sum(e for i, e in enumerate(a) if i % 2)

    ans = [0] * n
    ans[0] = x
    for i in range(1, n):
        ans[i] = 2 * a[i-1] - ans[i-1]
    print(*ans)

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""
1
4
-1 1 1 -1

"""

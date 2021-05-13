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
    # n, m = [int(x) for x in input().split()]
    n = int(input())
    a = [int(x) for x in input().split()]
    e = defaultdict(int)
    o = defaultdict(int)
    for i in range(n):
        if i % 2:
            e[a[i]] += 1
        else:
            o[a[i]] += 1
    ee = n // 2
    oo = n // 2 + 1
    x = [(e[el], el) for el in e] + [(0, 0)]
    y = [(o[el], el) for el in o] + [(0, 0)]
    x.sort(reverse=True)
    y.sort(reverse=True)
    ans = n
    if x[0][1] == y[0][1]:
        ans = min(ans, n - x[0][0] - y[1][0])
        ans = min(ans, n - x[1][0] - y[0][0])
    else:
        ans = n - x[0][0] - y[0][0]
    print(ans)

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

azyxwvutsrqponmlkjihgfedcb

"""

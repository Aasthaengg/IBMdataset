# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd, ceil, atan, pi
def input(): return sys.stdin.readline()[:-1] # warning not \n
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
    a = []
    for _ in range(n):
        x, l = [int(x) for x in input().split()]  
        s = x - l
        e = x + l
        a.append((s, e))
    a.sort(key=lambda x: x[1])
    ans = 0
    l = float('-inf')
    for s, e in a:
        if s >= l:
            l = e
        else:
            ans += 1
    print(n-ans)

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""
a b a
d c d
a b a
"""

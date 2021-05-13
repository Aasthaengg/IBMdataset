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
    d = defaultdict(int)
    for i in range(n):
        s = input()
        for e in s:
            d[e] += 1
    odd = 0
    q = 0
    for c in d:
        odd += d[c] % 2
        q += d[c] // 4
    if n % 2 and m % 2:
        if odd == 1 and q * 4 >= (n * m - (n + m - 1)):
            print("Yes")
        else:
            print("No")
    elif n % 2 != m % 2:
        ev = n
        if m % 2 == 0: ev = m
        if q * 4 < n * m - ev or odd:
            print("No")
        else:
            print("Yes")
    else:
        if q * 4 != n * m:
            print("No")
        else:
            print("Yes")


t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""
a b a
d c d
a b a
"""

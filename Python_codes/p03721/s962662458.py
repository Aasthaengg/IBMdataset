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
    n, k = [int(x) for x in input().split()]
    d = defaultdict(int)
    for _ in range(n):
        a, b = [int(x) for x in input().split()]
        d[a] += b
    a = [(x, d[x]) for x in d]
    a.sort()
    i = 0
    while k > a[i][1]:
        k -= a[i][1]
        i += 1

    print(a[i][0])

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

azyxwvutsrqponmlkjihgfedcb

"""

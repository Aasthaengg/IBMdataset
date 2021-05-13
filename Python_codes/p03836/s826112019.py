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
    a,b,x,y = [int(x) for x in input().split()]

    r = x - a
    u = y - b

    ans = ''

    ans += 'D'
    ans += 'R' * (r + 1)
    ans += 'U' * (u + 1)
    ans += 'L'
    ans += 'D' * u
    ans += 'L' * r

    ans += 'L'
    ans += 'U' * (u + 1)
    ans += 'R' * (r + 1)
    ans += 'D'
    ans += 'L' * r
    ans += 'D' * u

    print(ans)

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

azyxwvutsrqponmlkjihgfedcb

"""

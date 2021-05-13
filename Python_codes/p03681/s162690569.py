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

def fmod(x):
    ans = 1
    for i in range(1, x + 1):
        ans *= i
        ans %= MOD
    return ans

def solve():
    n, m = [int(x) for x in input().split()]
    n, m = min(n,m), max(n,m)
    x = m - n
    if x > 1:
        print(0)
    elif x == 1:
        print((fmod(n) * fmod(m))%MOD)
    else:
        print((fmod(n) * fmod(m)*2)%MOD)


t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

azyxwvutsrqponmlkjihgfedcb

"""

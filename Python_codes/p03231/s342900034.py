# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    n, m = [int(x) for x in input().split()]
    s = input()
    t = input()
    g = gcd(n, m)
    ans = n * m // g
    a, b = n // g, m // g
    x, y = 0, 0
    for i in range(g):
        if s[x] != t[y]:
            print(-1)
            return
        x += a
        y += b
    print(ans)
    
t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

2 2 2 2 2

"""

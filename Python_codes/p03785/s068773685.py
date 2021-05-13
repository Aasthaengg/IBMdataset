# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    n, c, k = [int(x) for x in input().split()]
    a = []
    for _ in range(n):
        a.append(int(input()))
    a.sort()
    ans = 0
    bus = 0
    deadline = 0
    for t in a:
        if t <= deadline and bus < c:
            bus += 1
        else:
            bus = 1
            ans += 1
            deadline = t + k
    print(ans)



t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

abc

"""

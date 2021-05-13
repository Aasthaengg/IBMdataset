# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = deque()
    for i in range(n):
        if i % 2:
            b.appendleft(a[i])
        else:
            b.append(a[i])
    if n % 2:
        b.reverse()
    print(*b)


t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

abc

"""

# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    n = int(input())
    a = [int(x)-1 for x in input().split()]
    ans = 0
    for i in range(n):
        if a[i] == i:
            if i + 1 < n:
                a[i], a[i+1] = a[i+1], a[i]
            else:
                a[i], a[i-1] = a[i-1], a[i]
            ans += 1

    print(ans)

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

abc

"""

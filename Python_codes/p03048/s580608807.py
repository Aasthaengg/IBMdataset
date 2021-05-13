# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    a,b,c,n = [int(x) for x in input().split()]
    d = [0] * 10000
    d[0] = 1
    for i in range(0,5000):
        d[i + a] += d[i]
    for i in range(0,5000):
        d[i + b] += d[i]
    for i in range(0,5000):
        d[i + c] += d[i]

    print(d[n])
    

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

1 + k



"""

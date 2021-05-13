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
    mn = min(a)
    while True:
        b = set()
        for e in a:
            if e % mn:
                b.add(e%mn)
            else:
                b.add(mn)
        a = list(b)
        mn = min(a)
        if len(a) == 1:
            print(mn)
            return
    

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

2 3 4 4
3 4 4
2 3 4
2 3 4
2 4 4


"""

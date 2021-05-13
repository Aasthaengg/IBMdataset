# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    n, p = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    o = 0
    e = 0
    for e in a:
        if e % 2:
            o += 1
        else:
            e += 1
    if o:
        print(2 ** (n-1))
    else:
        if p:
            print(0)
        else:
            print(2 ** n)
        


t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

"""

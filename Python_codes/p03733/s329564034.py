# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    n, h = [int(x) for x in input().split()]
    t = [int(x) for x in input().split()]
    total = 0
    off = 0
    for e in t:
        if e >= off:
            total += h
        else:
            total += h - (off - e)
        off = e + h
            
    print(total)
    

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

1 + k



"""

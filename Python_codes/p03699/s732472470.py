# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    n = int(input())
    a = []
    sm = 0
    for _ in range(n):
        x = int(input())
        if x % 10:
            a.append(x)
        sm += x
    a.sort()
    if sm % 10:
        print(sm)
    else:
        if a:
            sm -= a[0]
        else:
            sm = 0
        print(sm)
    
    

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

1 + k



"""

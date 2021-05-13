# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    n = int(input())
    s = set()
    for _ in range(n):
        a = int(input())
        if a not in s:
            s.add(a)
        else:
            s.remove(a)
    print(len(s))

    

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

1 + k



"""

# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    s = input()
    a = 0
    b = 0
    c = 0
    for e in s:
        if e == 'a':
            a += 1
        elif e == 'b':
            b += 1
        else:
            c += 1
    if abs(a - b) < 2 and abs(b - c) < 2 and abs(a - c) < 2:
        print("YES")
    else:
        print("NO")
        


t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

abc

"""

# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    w, h, x, y = [int(x) for x in input().split()]
    print((w*h)/2, int(w == 2 * x and h == 2 * y))

        



t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""



"""

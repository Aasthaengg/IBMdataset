# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    n, a, b = [int(x) for x in input().split()]
    print(max(0, ((n-1) * b + a) - ((n-1) * a + b) + 1))

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""



"""

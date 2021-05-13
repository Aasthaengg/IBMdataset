# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd, ceil
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')
import string
# string.ascii_lowercase
from bisect import bisect_left

def solve():
    n, m = [int(x) for x in input().split()]
    x = 1900 * m
    y = 100 * (n - m)
    print(2 ** m * (x + y))

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

azyxwvutsrqponmlkjihgfedcb

"""

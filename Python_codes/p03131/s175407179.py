# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    k, a, b = [int(x) for x in input().split()]
    if b - a > 2:
        # i need a - 1 ops to make 1 yen (and one biscuit for the operetion itself)
        # i need even number of ops (which are left now)
        # if there is odd number its just +1 to result
        ops = k - a + 1
        print(max(k + 1, (b - a) * (ops // 2) + a + (ops % 2)))

    else:
        print(k + 1)

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

1 + k



"""

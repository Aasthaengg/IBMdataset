# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    l, r = [int(x) for x in input().split()]
    if r - l + 1 >= 5000:
        print(0)
    else:
        M = 2019
        mn = []
        for i in range(l, r + 1):
            for j in range(i+1, r + 1):
                mn.append((i*j)%M)

        mn.sort()
        print(mn[0])
        



t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""



"""

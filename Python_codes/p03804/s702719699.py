# -*- coding: utf-8 -*-
import sys
# from collections import defaultdict, deque
from math import log10, sqrt, ceil
def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline()[:-1]


def solve():
    
    n, m = [int(x) for x in input().split()]
    a = []
    for i in range(n):
        a.append(input())
    b = []
    for i in range(m):
        b.append(input())

    ok = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            f = 1
            for x in range(m):
                for y in range(m):
                    if a[i+x][j+y] != b[x][y]:
                        f = 0
            ok |= f


    if ok:
        print("Yes")
    else:
        print("No")
        




t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()



"""
1 -> (1, 2) -> (2 ** 3, 3) -> (3, 1)
100000007
"""


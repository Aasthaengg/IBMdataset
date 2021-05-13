# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    n = int(input())
    b = [int(x) for x in input().split()]
    a = []
    for i in range(n):
        a.append((b[i], i))
    a.sort()
    ans = [0] * n
    m = n // 2


    for i in range(n):
        j = a[i][1]
        if i < m:
            ans[j] = (a[m][0])
        else:
            ans[j] = (a[m-1][0])

    for e in ans:
        print(e)


t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

2 3 4 4
3 4 4
2 3 4
2 3 4
2 4 4


"""

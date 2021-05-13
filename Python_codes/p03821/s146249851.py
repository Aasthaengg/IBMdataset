# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')

def top(x, y):
    return y * ((x + y - 1) // y)

def solve():
    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        x, y = [int(x) for x in input().split()]
        a[i] = x
        b[i] = y

    a.reverse()
    b.reverse()

    ans = 0
    pls = 0
    for i in range(n):
        a[i] += pls
        xd = top(a[i], b[i]) - a[i]
        ans += xd
        pls += xd
    print(ans)

    
t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

7
3 1
4 1
5 9
2 6
5 3
5 8
9 7 5

"""

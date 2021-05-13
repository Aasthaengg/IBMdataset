# -*- coding: utf-8 -*-
import sys
from collections import defaultdict, deque
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline()[:-1]

def check(d, x):
    c = 0
    while x % 100 == 0:
        x //= 100
        c += 1
    return c == d

def solve():
    d, n = [int(x) for x in input().split()]
    cnt = 0
    val = 0
    while cnt < n:
        val += 1
        if check(d, val): cnt += 1
    print(val)


t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()

"""

"""


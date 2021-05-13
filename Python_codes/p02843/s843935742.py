# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')


def solve():
    xd = [100, 101, 102, 103, 104, 105]
    mxn = int(1e5) + 1
    d = [0] * (mxn)
    d[0] = 1
    for e in xd:
        for i in range(mxn):
            if d[i] and i + e < mxn: d[i + e] = 1
    t = int(input())
    print(d[t])



t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

a aa c ca c a b a ab a b c

"""

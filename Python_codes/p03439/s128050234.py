#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007
flush = sys.stdin.flush()

def solve():
    n = I()
    print(0)
    flush
    s = input()
    l = 0
    r = n
    s0 = s
    while s != "Vacant":
        m = (l+r) >> 1
        print(m)
        flush
        s = input()
        if m&1:
            if s == s0:
                r = m
            else:
                l = m
        else:
            if s != s0:
                r = m
            else:
                l = m
    return

#Solve
if __name__ == "__main__":
    solve()

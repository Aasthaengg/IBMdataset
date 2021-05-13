#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from itertools import permutations
import sys
import math
import bisect
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

def solve():
    n = I()
    a = LI()
    m = max(a)
    M = min(a)
    if abs(M) <= abs(m):
        for i in range(n):
            if a[i] == m:
                break
        x = i+1
        print(2*n-1)
        for i in range(n):
            print(x,i+1)
        for i in range(n-1):
            print(i+1,i+2)
    else:
        for i in range(n):
            if a[i] == M:
                break
        x = i+1
        print(2*n-1)
        for i in range(n):
            print(x,i+1)
        for i in range(n-1)[::-1]:
            print(i+2,i+1)
    return

#Solve
if __name__ == "__main__":
    solve()

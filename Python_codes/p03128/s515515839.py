#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.buffer.readline().split()]
def I(): return int(sys.stdin.buffer.readline())
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
    W,n = LI()
    a = LI()
    for i in range(n):
        a[i] -= 1
    a.sort(reverse = True)
    b = [2,5,5,4,5,6,3,7,6]
    dp = [-float("inf")]*(W+1)
    dp[0] = 0
    for i in range(n):
        v = a[i]+1
        w = b[a[i]]
        for j in range(W):
            nj = j+w
            if nj > W:
                continue
            nd = dp[j]*10+v
            if dp[nj] < nd:
                dp[nj] = nd
    print(dp[W])
    return

#Solve
if __name__ == "__main__":
    solve()
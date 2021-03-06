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

def solve():
    n = I()
    d = LIR(n)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k]+d[k][j] < d[i][j]:
                    print(-1)
                    return
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(n):
                if k in (i,j):
                    continue
                if d[i][k]+d[k][j] <= d[i][j]:
                    break
            else:                
                ans += d[i][j]
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()

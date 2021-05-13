#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
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
    l = list(map(int, input()))
    n = len(l)
    dp = [[0]*2 for i in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        ni = i+1
        for j in range(2):
            x = 1 if j else l[i]
            for d in range(x+1):
                nj = j or d < l[i]
                if d:
                    dp[ni][nj] += 2*dp[i][j]
                else:
                    dp[ni][nj] += dp[i][j]
                dp[ni][nj] %= mod
    print(sum(dp[n])%mod)
    return

#Solve
if __name__ == "__main__":
    solve()

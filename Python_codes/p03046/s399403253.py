#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from itertools import permutations
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
    m,k = LI()
    if k == 0:
        print(*[i>>1 for i in range(1<<(m+1))])
        return
    if 1<<m <= k or m == k == 1:
        print(-1)
    else:
        ans = [k]+[i for i in range(1<<m) if i != k]+[k]+[i for i in range(1<<m)[::-1] if i != k]
        print(*ans)
    return

#Solve
if __name__ == "__main__":
    solve()

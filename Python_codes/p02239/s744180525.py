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
    v = []
    for i in range(n):
        e = LI()
        u = e[2:]
        for i in range(len(u)):
            u[i] -= 1
        v.append(u)
    d = [-1]*n
    d[0] = 0
    q = deque([0])
    while q:
        x = q.popleft()
        nd = d[x]+1
        for y in v[x]:
            if d[y] < 0:
                d[y] = nd
                q.append(y)
    for i in range(n):
        print(i+1,d[i])
    return

#Solve
if __name__ == "__main__":
    solve()


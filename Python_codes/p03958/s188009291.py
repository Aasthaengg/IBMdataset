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
    k,t = LI()
    a = LI()
    q = []
    for i in a:
        heappush(q,-i)
    while len(q) > 1:
        x = heappop(q)
        y = heappop(q)
        x += 1
        y += 1
        if x:
            heappush(q,x)
        if y:
            heappush(q,y)
    if not q:
        print(0)
    else:
        print(-q[0]-1)
    return

#Solve
if __name__ == "__main__":
    solve()

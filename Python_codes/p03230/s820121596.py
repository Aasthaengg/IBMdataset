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
    n = I()
    l = 1
    r = n
    while r > l+1:
        m = (l+r) >> 1
        if m*(m+1) >> 1 <= n:
            l = m
        else:
            r = m
    if l*(l+1) >> 1 < n:
        print("No")
        return
    print("Yes")
    f = [[1]]
    for i in range(l-1):
        a = f[-1][-1]+1
        f += [list(range(a,a+i+2))]
    k = l+1
    ans = [[i[-1] for i in f]]
    for i in range(l):
        p = f[i][:i]
        p += [f[j][i] for j in range(i,l)]
        ans += [p]
    print(k)
    for i in ans:
        print(len(i),*i)
    return

#Solve
if __name__ == "__main__":
    solve()

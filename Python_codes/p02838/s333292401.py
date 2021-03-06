#!usr/bin/env python3
from collections import defaultdict, deque, Counter, OrderedDict
from functools import reduce, lru_cache
import functools
import collections, heapq, itertools, bisect
import math, fractions
import sys, copy

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI1(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline().rstrip())
def LS(): return [list(x) for x in sys.stdin.readline().split()]
def S(): return list(sys.stdin.readline().rstrip())
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]
dire8 = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
MOD = 1000000007

def main():
    N = I()
    A = LI()

    C0, C1 = [0] * 60, [0] * 60

    for d in range(60):
        for ai in A:
            C0[d] += (ai >> d & 1) == 0
            C1[d] += (ai >> d & 1) == 1

    ans = 0
    for (d, (a, b)) in enumerate(zip(C0, C1)):
        ans = (ans + a * b * (1 << d % MOD)) % MOD
    print(ans % MOD)



if __name__ == '__main__':
    main()
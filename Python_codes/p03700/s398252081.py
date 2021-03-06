from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from operator import mul
from functools import reduce



sys.setrecursionlimit(2147483647)
INF = float('inf')
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 1000000007


n, a, b = LI()
L = IR(n)
ok = max(L) // b + 1
ng = 0
while ok > ng + 1:
    mid = (ok + ng) // 2
    remain = mid
    for i in range(n):
        remain -= max(0, (L[i] - b * mid) // (a - b) + bool((L[i] - b * mid) % (a - b)))
        if remain < 0:
            ng = mid
            break
    else:
        ok = mid



print(ok)
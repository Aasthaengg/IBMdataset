from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from itertools import permutations, accumulate, combinations, combinations_with_replacement
from math import sqrt, ceil, floor, factorial
from bisect import bisect_left, bisect_right, insort_left, insort_right
from copy import deepcopy
from operator import itemgetter
from functools import reduce
from fractions import gcd
import sys
def input(): return sys.stdin.readline().rstrip()
def I(): return int(input())
def Is(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def TI(): return tuple(map(int, input().split()))
def IR(n): return [I() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def TIR(n): return [TI() for _ in range(n)]
def S(): return input()
def Ss(): return input().split()
def LS(): return list(input())
def SR(n): return [S() for _ in range(n)]
def SsR(n): return [Ss() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
sys.setrecursionlimit(10**6)
MOD = 10**9+7
INF = 10**18
# ----------------------------------------------------------- #

n, m, q = Is()
LR = TIR(m)
PQ = TIR(q)

X = [[0]*(n+1) for _ in range(n+1)]
for l, r in LR:
    X[l][r] += 1

Acc = deepcopy(X)
for i in range(n+1):
    for j in range(n):
        Acc[i][j+1] += Acc[i][j]
for i in range(n):
    for j in range(n+1):
        Acc[i+1][j] += Acc[i][j]

# X[p][p] + X[p][p+1] + ... + X[p][q] + X[p+1][p] + ... + X[q][q]
# -> Acc[q][q] - Acc[q][p-1] - Acc[p-1][q] + Acc[p-1][p-1]

for p, q in PQ:
    ans = Acc[q][q] - Acc[q][p-1] - Acc[p-1][q] + Acc[p-1][p-1]
    print(ans)

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
INF = float('inf')
# ----------------------------------------------------------- #

n, A, B, C = Is()
L = IR(n)

def dfs(i, a, b, c):
    if i == n:
        return abs(A-a) + abs(B-b) + abs(C-c) - 30 if min(a, b, c) > 0 else INF
    ret0 = dfs(i+1, a, b, c)
    ret1 = dfs(i+1, a+L[i], b, c) + 10
    ret2 = dfs(i+1, a, b+L[i], c) + 10
    ret3 = dfs(i+1, a, b, c+L[i]) + 10
    return min(ret0, ret1, ret2, ret3)

print(dfs(0, 0, 0, 0))

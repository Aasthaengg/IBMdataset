from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from itertools import permutations, accumulate, combinations, combinations_with_replacement
from math import sqrt, ceil, floor, factorial
from bisect import bisect_left, bisect_right, insort_left, insort_right
from copy import deepcopy
from operator import itemgetter
from functools import reduce, lru_cache
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

h, w = Is()
s = LSR(h)
y = [1, 0]
x = [0, 1]

@lru_cache(None)
def dfs(sy, sx, gy, gx, ans, flag):
    if sy == gy and sx == gx:
        return 0
    for i in range(2):
        ny = sy + y[i]
        nx = sx + x[i]
        if 0 <= ny < h and 0 <= nx < w:
            if s[ny][nx] == '#':
                if flag:
                    ans = min(ans, dfs(ny, nx, gy, gx, ans, True))
                else:
                    ans = min(ans, dfs(ny, nx, gy, gx, ans, True)+1)
            else:  # s[ny][nx] == '.'
                ans = min(ans, dfs(ny, nx, gy, gx, ans, False))
    return ans

if s[0][0] == '.':
    print(dfs(0, 0, h-1, w-1, INF, False))
else:
    print(dfs(0, 0, h-1, w-1, INF, True)+1)

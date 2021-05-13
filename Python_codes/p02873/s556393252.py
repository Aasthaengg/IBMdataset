from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from itertools import permutations, accumulate, combinations, combinations_with_replacement, groupby
from math import sqrt, ceil, floor, factorial
from bisect import bisect_left, bisect_right, insort_left, insort_right
from copy import deepcopy
from operator import itemgetter
from functools import reduce, lru_cache  # @lru_cache(None)
from fractions import gcd
import sys
def input(): return sys.stdin.readline().rstrip()
def I(): return int(input())
def Is(): return (int(x) for x in input().split())
def LI(): return list(Is())
def TI(): return tuple(Is())
def IR(n): return [I() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def TIR(n): return [TI() for _ in range(n)]
def S(): return input()
def Ss(): return input().split()
def LS(): return list(S())
def SR(n): return [S() for _ in range(n)]
def SsR(n): return [Ss() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
sys.setrecursionlimit(10**6)
MOD = 10**9+7
INF = 10**18
# ----------------------------------------------------------- #

s = S()
A = [(key, sum(1 for _ in group)) for key, group in groupby(s)]
tmp = 0
ans = 0
for key, count in A:
    if key == '<':
        ans += count*(count+1)//2
        tmp = count
    else:
        if tmp < count:
            ans -= tmp
            ans += count*(count+1)//2
        else:
            ans += (count-1)*count//2
        tmp = 0
print(ans)

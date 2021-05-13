from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from functools import reduce



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


def comb(n, r):
    fact = 1
    for i in range(n - r + 1, n + 1):
        fact = fact * i
    divisor = 1
    for j in range(1, r + 1):
        divisor = divisor * j


    return fact // divisor



n, a, b = LI()
value = sorted(LI(), reverse=True)
m = value[a-1]
ans = 0
print(sum(value[:a]) / a)
left_cnt = value[:a].count(m)
total_cnt = value.count(m)
if left_cnt != a:
    print(comb(total_cnt, left_cnt))
else:
    for k in range(a, min(total_cnt, b) + 1):
        ans += comb(total_cnt, k)
    print(ans)
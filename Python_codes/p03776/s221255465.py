from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
from copy import deepcopy
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from operator import mul
from functools import reduce


sys.setrecursionlimit(2147483647)
INF = 10 ** 20
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
mod = 1000000007


def comb(n, k):
    if k > n:
        return 0
    x = 1
    for j in range(n - k + 1, n + 1):
        x = x * j
    for l in range(1, k + 1):
        x = x // l
    return x

n, a, b = LI()
V = LI()
V.sort(reverse=True)
s = V[a - 1]
cnt1 = V.count(s)
cnt2 = V[:a].count(s)
print(sum(V[:a]) / a)
if cnt2 != a:
    print(comb(cnt1, cnt2))
    exit()
ret = 0
for i in range(a, b + 1):
    ret += comb(cnt1, i)
    cnt2 += 1

print(ret)






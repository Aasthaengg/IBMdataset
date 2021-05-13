from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, gcd
from operator import mul
from functools import reduce
from operator import mul
from pprint import pprint
import numpy as np


sys.setrecursionlimit(2147483647)
INF = 10 ** 20
def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def I(): return int(sys.stdin.buffer.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 1000000007


n, k = LI()
A = np.array(LI(), dtype=np.int64)
bit_cnt = [((A >> k) & 1).sum() for k in range(40)]
ans = 0
for i in range(40):
    if k >> i & 1 == 0:
        continue
    ret = 0
    ret += bit_cnt[i] * (1 << i)
    for j in range(i + 1, 40):
        if k >> j & 1:
            ret += (n -  bit_cnt[j]) * (1 << j)
        else:
            ret += bit_cnt[j] * (1 << j)
    for l in range(i):
        ret += max(n - bit_cnt[l], bit_cnt[l]) * (1 << l)
    ans = max(ans, ret)


ret = 0
for a in A:
    ret += k ^ a

print(max(ret, ans))







from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
from pprint import pprint
from copy import deepcopy
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from operator import mul
from functools import reduce
from pprint import pprint


sys.setrecursionlimit(2147483647)
INF = 10 ** 13
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




h, w, k = LI()
fib_list = [1] * w
for i in range(2, w):
    fib_list[i] = fib_list[i - 1] + fib_list[i - 2]


dp = [[0] * w for _ in range(h + 1)]
dp[0][0] = 1
for i in range(h):
    for j in range(w):
        # そのまま行くパターン
        dp[i + 1][j] = (dp[i + 1][j] + dp[i][j] * fib_list[j] * fib_list[w - j - 1] % mod) % mod
        if j < w - 1:
            # 配るdp
            # 右側に配る
            dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j] * fib_list[j] * fib_list[w - j - 2] % mod) % mod
        if j > 0:
            # 左側に配る
            dp[i + 1][j - 1] = (dp[i + 1][j - 1] + dp[i][j] * fib_list[j - 1] * fib_list[w - j - 1] % mod) % mod




print(dp[-1][k - 1])

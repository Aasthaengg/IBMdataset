def getN():
    return int(input())
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]
def input():
    return sys.stdin.readline().rstrip()
def rand_N(ran1, ran2):
    return random.randint(ran1, ran2)
def rand_List(ran1, ran2, rantime):
    return [random.randint(ran1, ran2) for i in range(rantime)]
def rand_ints_nodup(ran1, ran2, rantime):
  ns = []
  while len(ns) < rantime:
    n = random.randint(ran1, ran2)
    if not n in ns:
      ns.append(n)
  return sorted(ns)

def rand_query(ran1, ran2, rantime):
  r_query = []
  while len(r_query) < rantime:
    n_q = rand_ints_nodup(ran1, ran2, 2)
    if not n_q in r_query:
      r_query.append(n_q)
  return sorted(r_query)

from collections import defaultdict, deque, Counter
from sys import exit
from decimal import *
import heapq
import math
from fractions import gcd
import random
import string
import copy
from itertools import combinations, permutations, product
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

#############
# Main Code #
#############

N, Ma, Mb = getNM()
query = [getList() for i in range(N)]

# dp[i][j][l]: i個まで探索したあとで物質aをjグラム,物質bをlグラム生成する最少費用
dp = [[[float('inf')] * 501 for i in range(501)] for i in range(N + 1)]
dp[0][0][0] = 0

# 各薬品
for i in range(N):
    # 物質a
    for j in range(501):
        # 物質b
        for l in range(501):
            a, b, c = query[i]
            if j - a >= 0 and l - b >= 0:
                dp[i + 1][j][l] = min(dp[i][j][l], dp[i][j - a][l - b] + c)
            else:
                dp[i + 1][j][l] = dp[i][j][l]

ans = float('inf')
for j in range(1, 500):
    for l in range(1, 500):
        if Ma * l == Mb * j and dp[N][j][l] < 10 ** 9 + 7:
            ans = min(ans, dp[N][j][l])
if ans < 10 ** 9 + 7:
    print(ans)
else:
    print(-1)
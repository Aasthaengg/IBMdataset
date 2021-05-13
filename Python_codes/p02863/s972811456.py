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

N, M = getNM()
query = [getList() for i in range(N)]

w = []
v = []
w_rev = []
v_rev = []
for i in range(N):
    w.append(query[i][0])
    v.append(query[i][1])
    w_rev.append(query[N - i - 1][0])
    v_rev.append(query[N - i - 1][1])

def knapsack_1(N, limit, weight, value):
    dp = [[0] * (limit + 1) for i in range(N + 1)]
    dp[0][0] = 0

    for i in range(N):
        for j in range(limit + 1):
            if weight[i] <= j:
                dp[i + 1][j] = max(dp[i][j], dp[i][j - weight[i]] + value[i])
            else:
                dp[i + 1][j] = dp[i][j]
    return dp

dp_1 = knapsack_1(N, M, w, v)
dp_2 = knapsack_1(N, M, w_rev, v_rev)

# 全ての料理について
ans = 0
for i in range(1, N + 1):
    opt = 0
    for j in range(M):
        if i == 1:
            o = query[i - 1][1] + dp_2[N - i][M - j - 1]
        elif i == N:
            o = dp_1[i - 1][j] + query[i - 1][1]
        else:
            # dp_1[i - 1][j] A[i]以前のものをj分以内に食べるナップサック
            # dp_2[N - i][M - j - 1] A[i]以降のものをM - j - 1分以内に食べるナップサック
            # dpにアクセスするだけなのでO(1)でいける
            o = dp_1[i - 1][j] + query[i - 1][1] + dp_2[N - i][M - j - 1]
        opt = max(opt, o)
    ans = max(ans, opt)
print(ans)
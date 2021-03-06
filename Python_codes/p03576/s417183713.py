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

N, K = getNM()
query = [getList() for i in range(N)]

# x軸, y軸を作る
x_axis = set()
y_axis = set()
for i in query:
    x_axis.add(i[0])
    y_axis.add(i[1])
x_axis = sorted(list(x_axis))
y_axis = sorted(list(y_axis))

# 経路圧縮
dp = [[0] * len(x_axis) for i in range(len(y_axis))]
for i in query:
    x = x_axis.index(i[0])
    y = y_axis.index(i[1])
    dp[y][x] += 1

dp_n = [[0] * len(x_axis) for i in range(len(y_axis))]

# 累積和
def bi_cumul_sum(dp_n, dp_bef, h, w):
    # 縦１行目、横１行目
    for i in range(h):
        dp_n[i][0] = dp_bef[i][0]
    for i in range(h):
        for j in range(1, w):
            dp_n[i][j] = dp_n[i][j - 1] + dp_bef[i][j]
    # 全て
    for i in range(1, h):
        for j in range(w):
            dp_n[i][j] += dp_n[i - 1][j]

bi_cumul_sum(dp_n, dp, len(y_axis), len(x_axis))

# 範囲内に含まれる点の数を計算する
def judge(sx, ex, sy, ey, dp):
    mother = dp[ey][ex]
    minus1 = 0
    minus2 = 0
    plus = 0
    if sx > 0:
        minus1 = dp[ey][sx - 1]
    if sy > 0:
        minus2 = dp[sy - 1][ex]
    if sx > 0 and sy > 0:
        plus = dp[sy - 1][sx - 1]
    return mother - minus1 - minus2 + plus

ans = float('inf')
for sy in range(len(y_axis)):
    for ey in range(sy, len(y_axis)):
        for sx in range(len(x_axis)):
            for ex in range(sx, len(x_axis)):
                if judge(sx, ex, sy, ey, dp_n) >= K:
                    opt = (x_axis[ex] - x_axis[sx]) * (y_axis[ey] - y_axis[sy])
                    ans = min(ans, opt)
print(ans)
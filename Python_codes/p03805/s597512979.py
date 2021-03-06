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
from heapq import heapify, heappop, heappush
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from operator import mul, itemgetter
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

#############
# Main Code #
#############

"""
全ての場所を一度だけ通り巡回する通りの数
bit(1 << N)を小さい順から探索する
①bit & (1 << 0)
最初に0を踏んでないということだから飛ばす
②現在の場所sを探すためN個探索する
③次の場所tを探すためN個探索する
④渡すdpする
"""

N, M = getNM()
G = [[0] * N for i in range(N)]
for i in range(M):
    a, b = getNM()
    G[a - 1][b - 1] = 1 # a ~ bのエッジが存在する
    G[b - 1][a - 1] = 1

# 状態bitから次の状態へ渡すdpするというのはよくやる
# [0](001) → [0, 1](011) → [0, 1, 2](111)
#          → [0, 2](101) → [0, 1, 2](111)
def counter(sta):
    # dp[bit][i]これまでに踏んだ場所がbitであり、現在の場所がiである
    dp = [[0] * N for i in range(1 << N)]
    dp[1 << sta][sta] = 1

    for bit in range(1, 1 << N):
        if not bit & (1 << sta):
            continue
        # s:現在の場所
        for s in range(N):
            # sを踏んだことになっていなければ飛ばす
            if not bit & (1 << s):
                continue
            # t:次の場所
            for t in range(N):
                # tを過去踏んでいない and s → tへのエッジがある
                if (bit & (1 << t)) == 0 and G[s][t]:
                    dp[bit|(1 << t)][t] += dp[bit][s]

    return sum(dp[(1 << N) - 1])

print(counter(0))
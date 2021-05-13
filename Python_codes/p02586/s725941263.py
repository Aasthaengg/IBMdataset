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
from math import sqrt
from fractions import gcd
import random
import string
import copy
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

R, C, K = getNM()
point = [[0] * C for i in range(R)]
for i in range(K):
    r, c, v = getNM()
    point[r - 1][c - 1] = v

# dp[j][n] j列目にn個まで取った時の最大値
# 蟻本で出てた、前と後のdpを取り替える作業をしないと盛大にTLEる
prev = [[0] * 4 for _ in range(C + 1)]

for i in range(R):
    next = [[0] * 4 for _ in range(C + 1)]
    for j in range(C):
        # ①取った時
        # n = 2, n = 1, n = 0と逆順にやらないとバグる
        # (n = 0の処理を先に行うと、n = 1の時「変更後の」n = 0で計算を行ってしまうため)
        # (つまりpoint[i][j]のアイテムを何回も取得するため）
        
        # ②より扱うjの数が小さくなるので先に処理する
        # (こちらは②でprev[j + 1][n]の計算をする時「変更後の」prev[j][n]で計算する必要があるため）
        for n in range(2, -1, -1):
            prev[j][n + 1] = max(prev[j][n + 1], prev[j][n] + point[i][j])

        # ②取らない時
        for n in range(4):
            prev[j + 1][n] = max(prev[j + 1][n], prev[j][n])

        # ③下段に降りた時
        next[j][0] = max(prev[j])

    # dpの取り替え
    prev = next

print(max(prev[C - 1]))
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

H, W = getNM()
S = [input() for i in range(H)]
score_w = [[0] * W for i in range(H)]
score_h = [[0] * W for i in range(H)]

for i in range(H):
    now = -1
    for j in range(W):
        if now == -1:
            # 初期化
            if S[i][j] == '.':
                now = 1
                score_w[i][j] = now
        else:
            # 次が.の時
            if S[i][j] == '.':
                now += 1
                score_w[i][j] = now
            # 次が#の時
            else:
                now = -1

    for j in range(1, W):
        if score_w[i][-j - 1] > 0:
            score_w[i][-j - 1] = max(score_w[i][-j - 1], score_w[i][-j])

for j in range(W):
    now = -1
    for i in range(H):
        if now == -1:
            # 初期化
            if S[i][j] == '.':
                now = 1
                score_h[i][j] = now
        else:
            # 次が.の時
            if S[i][j] == '.':
                now += 1
                score_h[i][j] = now
            # 次が#の時
            else:
                now = -1

    for i in range(1, H):
        if score_h[-i - 1][j] > 0:
            score_h[-i - 1][j] = max(score_h[-i - 1][j], score_h[-i][j])

ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            ans = max(ans, score_w[i][j] + score_h[i][j] - 1)
print(ans)
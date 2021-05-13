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
from operator import mul, itemgetter
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

#############
# Main Code #
#############

# グラフが単純⇔グラフがループや多重辺をもたない
# グラフが連結⇔グラフの任意の２頂点に対し、それらを結ぶパス(辺)が存在
# 1 - 3 - 2
# 1 - 3
# |   |
# 2 - 4

# ある整数Sが存在して、任意の頂点についてその頂点に隣接する頂点の番号の値の和はSとなる
# このSは都合の良いもので設定できる

# まず全部繋ぐ N = 5の時
# 5: 1 2 3 4
# 4: 1 2 3 5
# 3: 1 2 4 5
# 2: 1 3 4 5
# 1: 2 3 4 5
# sumから何かを引いたら何かになる

N = getN()
dist = set()
if N % 2 == 0:
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i != j and i + j != (N + 1):
                dist.add((min(i, j), max(i, j)))
if N % 2 != 0:
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i != j and i + j != N:
                dist.add((min(i, j), max(i, j)))

dist = list(dist)
print(len(dist))
for a, b in dist:
    print(a, b)

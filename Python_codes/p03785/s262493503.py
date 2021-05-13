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

# 客:N人　バスの定員:C人　limit:K分
N, C, K = getNM()
T = getArray(N)
T.sort()

pas = 1
time = T[0]
ans = 1

for i in range(1, N):
    # 乗客が満杯だと
    if pas >= C:
        # バス増便
        ans += 1
        pas = 1
        time = T[i]
        continue

    # i人目を乗せた時制限時間を過ぎるようなら
    if T[i] > time + K:
        # バス増便
        ans += 1
        pas = 1
        time = T[i]
        continue

    # 上の二つの条件に引っかからないなら
    pas += 1

print(ans)
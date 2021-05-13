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

S = input()
N = len(S)

dp = [[0] * 13 for i in range(N)]
str_int = '0123456789'
if S[0] in str_int:
    dp[0][int(S[0])] += 1
else:
    for i in range(10):
        dp[0][i] += 1

for i in range(1, N):
    if S[i] in str_int:
        # 前の段
        for j in range(13):
            dp[i][(10 * j + int(S[i])) % 13] += (dp[i - 1][j] % mod)
    else:
        # 前の段
        for j in range(13):
            # 後ろの段
            # ?なら0 ~ 10で回す
            for l in range(10):
                dp[i][(10 * j + l) % 13] += (dp[i - 1][j] % mod)

print(dp[N - 1][5] % mod)
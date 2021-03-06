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

N, M = getNM()
S = getList()
N_s = len(S)
T = getList()
N_t = len(T)

dp = [[0] * (N_s + 1) for i in range(N_t + 1)]
dp[0][0] = 0

for i in range(N_t):
    for j in range(N_s):
        # 基礎 dp[i][j] + Sを伸ばして増えた分 + Tを伸ばして増えた分
        dp[i + 1][j + 1] = (dp[i + 1][j] + dp[i][j + 1] - dp[i][j]) % mod
        if S[j] == T[i]:
            # dp[i][j]の通りのそれぞれの末尾に(S[i], T[i])をつけることで
            # dp[i][j]通り（と空に(S[i], T[i])をつけた）分新しいのが作れる
            dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j] + 1) % mod
print((dp[N_t][N_s] + 1) % mod)
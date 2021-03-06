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

L = input()

def digit_dp_2(n):
    l = len(n)

    dp = [[[0] * 2 for _ in range(2)] for i in range(l + 1)]
    dp[0][0][0] = 1

    for i in range(l):
        d = int(n[i])

        # Lになる可能性があるかないか
        for j in range(2):
            # 次の桁が0か1か
            for d_j in range(2 if j else d + 1):
                if d_j == 0:
                    dp[i + 1][j | (d_j < d)][d_j] += (dp[i][j][0] + dp[i][j][1])
                    dp[i + 1][j | (d_j < d)][d_j] %= mod
                else:
                    dp[i + 1][j | (d_j < d)][d_j] += 2 * (dp[i][j][0] + dp[i][j][1])
                    dp[i + 1][j | (d_j < d)][d_j] %= mod

    return sum(dp[-1][0]) + sum(dp[-1][1])

print(digit_dp_2(L) % mod)
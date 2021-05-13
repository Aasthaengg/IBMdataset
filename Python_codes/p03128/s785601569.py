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
from math import sqrt, pi
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

num = [2, 5, 5, 4, 5, 6, 3, 7, 6]

N, M = getNM()
A = getList()

digit = []
for i in A:
    digit.append([i, num[i - 1]])
digit.sort(key = lambda i: i[1])

dp = [-float('inf')] * (N + 1)
dp[0] = 0

# 桁数を調べる
for i in range(1, N + 1):
    for j in range(M):
        if i >= digit[j][1]:
            dp[i] = max(dp[i], dp[i - digit[j][1]] + 1)

# 数字を組み上げる
ans = ''
now = N
digit.sort(reverse = True)
while now > 0:
    for j in range(M):
        if now - digit[j][1] >= 0 and dp[now] == dp[now - digit[j][1]] + 1:
            now -= digit[j][1]
            ans += str(digit[j][0])
            break
print(ans)
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

"""
6
40 1 30 2 7 20
"""

N = getN()
A = getList()
A.sort()
imos = copy.deepcopy(A)
for i in range(N - 1):
    imos[i + 1] += imos[i]

# 自分より小さい怪物を全て飲み込んだときに一つ上の怪物を飲み込めるか
streak = [0] * N
streak[-1] = 1
for i in range(N - 1):
    if imos[i] * 2 >= A[i + 1]:
        streak[i] = 1

ans = 0
for i in range(N - 1, -1, -1):
    if streak[i] == 1:
        ans += 1
    else:
        break
print(ans)
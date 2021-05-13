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

A = input()
Ac = Counter(A)
cnt = 0
# 前からdp等して数え上げするか
# グルーピングして掛け算するか

# A = 'babab'だった場合
# (1, 2):abbab
# (1, 3):babab
# (1, 4):ababb
# (1, 5):babab

# (2, 3):bbaab
# (2, 4):babab
# (2, 5):bbaba

# (3, 4):babba
# (3, 5):babab

# (4, 5):babab

# i < jでAi = Ajだった場合、
# Ai+1 と Aj-1とで結果がダブる
for val in Ac.values():
    cnt += val * (val - 1) // 2
print(len(A) * (len(A)-1) // 2 - cnt + 1)
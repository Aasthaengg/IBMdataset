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
from heapq import heapify, heappop, heappush
import math
import random
import string
from copy import deepcopy
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

H, W, A, B = getNM()

"""
0, ?の場合は対応可能

0 0 0 1 1
0 0 0 1 1
0 0 0 1 1
0 0 0 1 1
0 0 0 1 1

対応出来ないケース無さそう？
1, 2の場合は？

これは1, 2
1 1 1 1 0
1 1 1 1 0
0 0 0 0 1
0 0 0 0 1
0 0 0 0 1
"""

res = [[''] * W for i in range(H)]

for i in range(H):
    for j in range(W):
        if (i < B) ^ (j < A):
            res[i][j] = str(0)
        else:
            res[i][j] = str(1)
res = [''.join(i) for i in res]
for i in res:
    print(i)
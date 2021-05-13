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

# Li-1 = [Li // A[i]] * A[i]
# Ri-1 = [Ri // A[i]] * A[i] + A[i] - 1

K = getN()
A = getList()
A = A[::-1]
if A[0] != 2:
    print(-1)
    exit()
mi = A[0]
mx = A[0] * 2 - 1
for i in range(1, K):
    ai = A[i]
    mi = (mi + ai - 1) // ai
    mx = mx // ai
    if mi > mx:
        print(-1)
        exit()
    else:
        mi = mi * ai
        mx = (mx + 1) * ai - 1
print(mi, mx)
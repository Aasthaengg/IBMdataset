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

M = getN()
A = getList()
plus = []
minus = []
for i in A:
    if i >= 0:
        plus.append(i)
    else:
        minus.append(i)
plus.sort()
minus.sort(reverse = True)

if len(minus) == 0:
    print(sum(plus) - 2 * min(plus))
    now = plus[0]
    for i in range(1, M - 1):
        print(now, plus[i])
        now = now - plus[i]
    print(plus[M - 1], now)
    exit()

if len(plus) == 0:
    print(-sum(minus) + 2 * max(minus))
    now = minus[0]
    for i in range(1, M):
        print(now, minus[i])
        now = now - minus[i]
    exit()

print(sum(plus) - sum(minus))
now = minus[0]
for i in range(1, len(plus)):
    print(now, plus[i])
    now = now - plus[i]

print(plus[0], now)
now = plus[0] - now

for i in range(1, len(minus)):
    print(now, minus[i])
    now = now - minus[i]
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

# d = 2 ** N - 1について
# 1 xor 2 xor... xor dは
# 各桁にフラグが2 * (N - 1)本ずつ立っている（つまり0になる）
# なのでXを抜くとXを構成する部分についてフラグが抜けてXができる

M, K = getNM()

if M == 0 and K == 0:
    print(0, 0)

elif M == 1 and K == 0:
    print(0, 0, 1, 1)

elif M >= 2 and K < 2 ** M:
    ans = []
    for n in range(2 ** M):
        if n != K:
            ans.append(n)
    print(*ans, K, *ans[::-1], K)
    
else:
    print(-1)
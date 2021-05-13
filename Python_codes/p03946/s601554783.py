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
from itertools import permutations
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7


#############
# Main Code #
#############

# print(rand_List(1, 10, 10))
N, T = getNM()
price = getList()
max_list = [0] * N

# この先訪れる店の中で最も値段が高い店の値段
def maximizer(num_list):
    num_N = len(num_list)
    res = 0
    for i in range(1, num_N + 1):
        res = max(res, price[-i])
        num_list[-i] = res
maximizer(max_list)

# 最大マージンを調べる
def margin_checker():
    margin = 0
    for i in range(N - 1):
        margin = max(max_list[i] - price[i], margin)
    return margin

max_margin = margin_checker()

cnt = 0
# ループはしないはず
while True:
    for i in range(N - 1):
        if max_list[i] - price[i] == max_margin:
            price[i] += 1
            cnt += 1
    if margin_checker() < max_margin:
        break
    # ループはしないはずだが念の為
    maximizer(max_list)
    max_margin = margin_checker()
print(cnt)
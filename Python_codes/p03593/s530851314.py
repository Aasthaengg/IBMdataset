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

H, W = getNM()
maze = [input() for i in range(H)]

dict = defaultdict(int)
for i in range(H):
    for s in maze[i]:
        dict[s] += 1

one_cnt = 0
two_cnt = 0
for i in dict.items():
    opt = i[1] % 4
    if opt == 1:
        one_cnt += 1
    elif opt == 2:
        two_cnt += 1
    elif opt == 3:
        one_cnt += 1
        two_cnt += 1

# 両方奇数
if H % 2 != 0 and W % 2 != 0:
    if one_cnt > 1 or two_cnt > H // 2 + W // 2:
        print('No')
        exit()
# Hが奇数
elif H % 2 != 0 and W % 2 == 0:
    if one_cnt > 0 or two_cnt > W // 2:
        print('No')
        exit()
# Wが奇数
elif H % 2 == 0 and W % 2 != 0:
    if one_cnt > 0 or two_cnt > H // 2:
        print('No')
        exit()
# 両方偶数
else:
    if one_cnt > 0 or two_cnt > 0:
        print('No')
        exit()
print('Yes')

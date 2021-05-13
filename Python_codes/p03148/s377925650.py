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

N, K = getNM()
various = defaultdict(list)
que = [getList() for i in range(N)]

ans = 0
num = []
var_s = set()

# 美味しい順にK個とった時の幸福度
que.sort(reverse = True, key = lambda i: i[1])
for i in range(K):
    ans += que[i][1]
    # もし２番手以降ならあとで交換する用にとっておく
    if que[i][0] in var_s:
        num.append(que[i][1])
    var_s.add(que[i][0])

var = len(var_s)
ans += var ** 2

# 使ってない種類について各種類で一番大きさが大きいもの
left_l = defaultdict(int)
for i in range(N):
    if not que[i][0] in var_s:
        left_l[que[i][0]] = max(left_l[que[i][0]], que[i][1])

num.sort(reverse = True)
left_l = [i[1] for i in left_l.items()]
left_l.sort()

# M回交換する
opt = ans
M = min(len(num), len(left_l))
for i in range(M):
    u = num.pop()
    s = left_l.pop()
    # 寿司単体の幸福度
    opt -= (u - s)
    # 種類が増える分
    opt += 2 * var + 1
    var += 1
    ans = max(opt, ans)

print(ans)
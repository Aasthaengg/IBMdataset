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

N, M = getNM()
dist = [[] for i in range(N)]
for i in range(M):
    l, r, d = getNM()
    dist[l - 1].append([r - 1, d])
    dist[r - 1].append([l - 1, -d])

dis = [float('inf')] * N

pos = deque([i for i in range(N)])
while len(pos) > 0:
    u = pos.popleft()
    # 始めの第一歩
    if dis[u] == float('inf'):
        dis[u] = 0
    # 行き先の位置が未確定なら確定させる
    # 既に確定しているなら判定
    for to, d in dist[u]:
        if dis[to] == float('inf'):
            dis[to] = dis[u] + d
            # 位置をレコードした頂点を優先的に処理する必要があるためappendleft
            # 例 que = [0, 2, 1], [1, 2, 3]
            # pos = [0, 1, 2] の時
            # dis = [0, -2, 1]でYesになるはず
            # 0を探索, 1の距離をレコードしてappend disは[0, inf, 1]
            # pos = [1, 2, 2]のため次は1を探索
            # dis[1] == infなのでdis[1] = 0にする
            # dis[1] = 0, dis[2] = 1なのでNo
            pos.appendleft(to)
        else:
            if dis[u] + d != dis[to]:
                print('No')
                exit()
print('Yes')
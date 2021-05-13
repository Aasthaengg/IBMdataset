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
from math import sqrt, pi
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
L = [getList() for i in range(N)]

# 寿司を美味しさの順に並べる
various = defaultdict(int)
L.sort(key = lambda i: i[1], reverse = True)

pool_der = []
ans = 0
# 美味しい順にK個取る
for i in range(K):
    t, d = L[i]
    # 種類をレコードする
    various[t] += 1
    # もし同じ種類のものを既に取っていたら
    if various[t] > 1:
        pool_der.append(d)
    ans += d
# 美味しい順にソートする
pool_der.sort(reverse = True)

# 現在の種類の数
now = len(various.items())
ans += now ** 2
L = L[K:]

# まだ出ていない種類の寿司の中で最大値を取るものをレコードする
pool_var = []
for i in L:
    # まだ登場していないなら
    # 2番手以下は必要ない
    if various[i[0]] == 0:
        pool_var.append(i[1])
        various[i[0]] += 1
# 後ろから美味しい順にソートする
pool_var.sort()

# 取っても種類数が変わらない寿司を取り、新たな種類の寿司を取る
point = ans
M = min(len(pool_der), len(pool_var))

for _ in range(M):
    der = pool_der.pop()
    var = pool_var.pop()

    point += (var - der)
    point += 2 * now + 1
    now += 1
    ans = max(ans, point)
print(ans)
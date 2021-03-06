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

# レベルNバーガーの下からX層目まで
N, X = getNM()

# レベルNバーガーの中間地点、全体のサイズ
cnt_burger = [[0 for i in range(2)] for i in range(51)]
cnt_burger[0] = [1, 1]
for i in range(1, 51):
    cnt_burger[i][0] = 1 + cnt_burger[i - 1][1] + 1
    cnt_burger[i][1] = cnt_burger[i][0] + cnt_burger[i - 1][1] + 1

# レベルNバーガーにパティが何枚含まれる？
cnt_patty = [0] * 51
cnt_patty[0] = 1
for i in range(1, 51):
    cnt_patty[i] = 2 * cnt_patty[i - 1] + 1

# レベルNの下からX番目までにパティが何枚含まれるか
# xが大きいのでdpはできない
def count(n, x):
    # レベル0バーガーの場合
    if n == 0 and x == 1:
        return 1

    # バーガーの一番下のパンのみ食べる場合
    if x == 1:
        return 0

    # 中間地点以前のどこかまで食べる場合
    elif 1 < x < cnt_burger[n][0]:
        # レベルn - 1バーガーの下からx - 1層目まで
        return count(n - 1, x - 1)

    # 中間地点まで食べる
    elif x == cnt_burger[n][0]:
        return cnt_patty[n - 1] + 1

    # 中間地点 ~ 最後以前のうちのどこか
    elif cnt_burger[n][0] < x < cnt_burger[n][1]:
        return cnt_patty[n - 1] + 1 + count(n - 1, x - cnt_burger[n][0])

    # 最後
    else:
         return 2 * cnt_patty[n - 1] + 1

print(count(N, X))
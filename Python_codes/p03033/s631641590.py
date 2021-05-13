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

# 各queryについてO(n)で答える
# 問題を言い換えると　　

# 地点Xに到着するのは時間 Di + Xの時
# S <= Di + X < Tとなる[S, T, N]がなければ通過できる
# SについてXの早い順にソートする

# 各Dについて、どのSまで通過できるかを各O(1)で答える？

N,Q = getNM()
# taskに
# 0:通行止め時間帯のスタート
# 1:通行止め時間帯のゴール
# 2:人
# を入れ、全部まとめて処理する
task = []

STX = [getList() for _ in range(N)]
for s, t, x in STX:
    task.append((t - x, 0, x)) # xで止まらなくなる
    task.append((s - x, 1, x)) # xで止まる

for i in range(Q):
    d = getN()
    task.append((d, 2, i)) # 止まる位置を答える
answer = [-1] * Q

task.sort()

# 引っかかってる場所の管理
se = set()
se_hp = [] # heapで最小値を先頭に保つ
heapq.heapify(se_hp)

# 小さい時刻から順に見ていく
# 人ciについてどの範囲cjの範囲内に入っているか
for a, b, c in task:
    # ゴール位置についての情報なら
    if b == 0:
        # そのゴールに対応するスタート位置を取り除く
        se.remove(c)
    # スタートについての情報なら
    elif b == 1:
        # スタート位置を追加する
        se.add(c)
        # スタート位置の最小値候補に入れる
        heapq.heappush(se_hp, c)
    # 人についての情報なら
    else:
        # se_hpの最小値がseにない（用済みのものが残っている）間
        # またはse_hpを抜き切るまで
        while se_hp and se_hp[0] not in se:
            heapq.heappop(se_hp)
        if se_hp:
            answer[c] = se_hp[0]
        else:
            answer[c] = -1
    # (-3, 1, 10) 10のものについてスタートを追加
    # se:{10} se_hp:[10]
    # (-1, 1, 2) 2のものについてスタートを追加
    # se:{10, 2} se_hp:[2, 10]
    # (0, 2, 0) 人0について調べる
    # se:{10, 2} se_hp[2, 10]
    # (1, 0, 2) 2のものについてゴールが来たのでスタート位置を取り除く
    # se:{10} se_hp:[2, 10] se_hpに余計なものが残る
    # (1, 1, 2) 2のものについてスタート位置をまた追加
    # se:{10, 2} se_hp:[2, 10, 2]

for i in answer:
    print(i)
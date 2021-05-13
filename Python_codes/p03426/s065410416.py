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

# Dかそれぞれのqueryで固定なのでこの問題は解ける
H, W, D = getNM()
maze = []
for i in range(H):
    a = getList()
    maze.append(a)
Q = getN()
# piece[0]からpiece[1]まで
# 4 → 6　→ 8
piece = []
for i in range(Q):
    l, r = getNM()
    piece.append([l, r])

place_list = [[-1, -1] for i in range(H * W)]

for y in range(H):
    for x in range(W):
        place_list[maze[y][x] - 1] = [x, y]

# 飛ばし累積和
x_plus = []
y_plus = []
for i in range(D):
    list_x = [0]
    list_y = [0]
    for j in range(i, H * W, D):
        if j == i:
            opt_x = 0
            opt_y = 0
        else:
            opt_x = abs(place_list[j][0] - place_list[j - D][0])
            opt_y = abs(place_list[j][1] - place_list[j - D][1])
        list_x.append(list_x[-1] + opt_x)
        list_y.append(list_y[-1] + opt_y)
    list_x.pop(0)
    list_y.pop(0)
    x_plus.append(list_x)
    y_plus.append(list_y)

def past_exam(piece_query):
    start = piece_query[0]
    goal = piece_query[1]

    mul = (start - 1) % D
    if D == 1:
        x_point = x_plus[0][goal - 1] - x_plus[0][start - 1]
        # 書き間違い!!
        y_point = y_plus[0][goal - 1] - y_plus[0][start - 1]
    else:
        x_point = x_plus[mul][(goal - mul) // D] - x_plus[mul][(start - mul) // D]
        y_point = y_plus[mul][(goal - mul) // D] - y_plus[mul][(start - mul) // D]
    return x_point + y_point

for i in range(Q):
    print(past_exam(piece[i]))
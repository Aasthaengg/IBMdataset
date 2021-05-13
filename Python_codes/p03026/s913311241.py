from _collections import deque
from _ast import Num


def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield (number)


input_parser = parser()


def gw():
    global input_parser
    return next(input_parser)


def gi():
    data = gw()
    return int(data)


MOD = int(1e9 + 7)

import numpy
from collections import deque
from math import sqrt
from math import floor
import heapq
# https://atcoder.jp/contests/agc033/tasks/agc033_b
# B - LRUD Game
"""
"""
N = gi()
t = [[] for i in range(N + 5)]

for i in range(1, N):
    a = gi()
    b = gi()
    t[a].append(b)
    t[b].append(a)
cs = [0] * N
for i in range(N):
    cs[i] = gi()
cs.sort()
print(sum(cs) - max(cs))
vs = [0] * (N + 5)
ci = N - 1
q = deque()
q.append(1)

while len(q):
    v = q.pop()
    # print(v, ci)
    vs[v] = cs[ci]
    ci -= 1
    for u in t[v]:
        if vs[u]:
            continue
        else:
            q.append(u)
for i in range(1, N + 1):
    print("%d " % (vs[i]), end="")

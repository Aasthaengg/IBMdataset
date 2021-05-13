# -*- coding: utf-8 -*-
import numpy as np
from collections import deque
from collections import defaultdict
import heapq
import collections
import itertools
import bisect


def zz():
    return list(map(int, input().split()))


def z():
    return int(input())


def S():
    return input()


def C(line):
    return [input() for _ in range(line)]


N, M = zz()
P, Y = [], []
years = defaultdict(list)
ids = defaultdict(list)
# years: [city_id, year]
for i in range(M):
    p, y = zz()
    years[p].append(y)
    ids[p].append(i)
# print(years)
ans = ['']*M
for p in years:
    c = zip(years[p], ids[p])
    c = sorted(c)
    year, id = zip(*c)
    for i, id_ in enumerate(id):
        i = i + 1
        ans[id_] = str(p).zfill(6) + str(i).zfill(6)
for a in ans:
    print(a)
# print(*ans)

# .zfill(6)

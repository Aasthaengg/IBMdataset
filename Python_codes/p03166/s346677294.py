from sys import stdin
import sys
import math
from functools import reduce
import functools
import itertools
from collections import deque,Counter
from operator import mul
import copy
# ! /usr/bin/env python
# -*- coding: utf-8 -*-
import heapq
sys.setrecursionlimit(10**6)

## a, bを無向辺として，隣接リストを作成
n, m = list(map(int, input().split()))
al = [[] for i in range(n)]

for i in range(m):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1

    al[a].append(b)

@functools.lru_cache(None)
def depth(u):
    if len(al[u]) == 0:
        return 0
    else:
        max_d = 0
        for v in al[u]:
            max_d = max(max_d, depth(v) + 1)
        return max_d

ans = 0
for i in range(n):
    ans = max(ans, depth(i))
print(ans)

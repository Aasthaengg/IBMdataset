from collections import Counter, deque
from fractions import gcd
from functools import lru_cache
from functools import reduce
import functools
import heapq
import itertools
import math
import numpy as np
import re
import sys

sys.setrecursionlimit(10000)
INF = float('inf')


def cummax(li, first=-float('inf')):
    """
    累積 max
    :param collections.Iterable li:
    :param float first:
    :return:
    """
    cm = first
    ret = []
    for v in li:
        cm = max(v, cm)
        ret.append(cm)
    return ret


N, C = list(map(int, input().split()))
X, V = zip(*[list(map(int, input().split())) for _ in range(N)])

X = np.array(X)
V = np.array(V)

# cs1[i]: 時計回りに i 番目まで食べたときの累計カロリー
cs1 = V.cumsum() - X
# 累積 max
cm1 = np.array(cummax(cs1, first=0))

# cs2[i]: 反時計回りに i 番目まで食べたときの累計カロリー
cs2 = V[::-1].cumsum() - (C - X)[::-1]
# 累積 max
cm2 = np.array(cummax(cs2, first=0))
cs2 = cs2[::-1]
cm2 = cm2[::-1]

ans = max(cm1.max(), cm2.max())
# 時計回りに X[L] まで行って、折り返して反時計回りに X[r] まで行く
r = 0
for L in range(len(X)):
    while r < len(X) and X[r] < X[L] * 2:
        r += 1
    if r < len(X):
        ans = max(ans, cm1[L] + cm2[r] - X[L])
    else:
        break
# 反時計回りが先
L = len(X) - 1
for r in reversed(range(len(X))):
    while L >= 0 and X[L] > C - (C - X[r]) * 2:
        L -= 1
    if L >= 0:
        ans = max(ans, cm2[r] + cm1[L] - (C - X[r]))
    else:
        break
print(ans)

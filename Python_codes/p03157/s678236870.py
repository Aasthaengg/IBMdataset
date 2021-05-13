import bisect
import heapq
import itertools
import math
import operator
import os
import re
import string
import sys
from collections import Counter, deque, defaultdict
from copy import deepcopy
from decimal import Decimal
from fractions import gcd
from functools import lru_cache, reduce
from operator import itemgetter, mul, add, xor

import numpy as np
from scipy.misc import comb

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7

H, W = list(map(int, sys.stdin.readline().split()))
S = [list(sys.stdin.readline().rstrip()) for _ in range(H)]
seen = np.zeros((H, W), dtype=bool)


def dfs(h, w):
    if seen[h][w]:
        return 0, 0
    seen[h][w] = True
    black = int(S[h][w] == '#')
    white = int(S[h][w] == '.')
    for dh, dw in zip([h, h, h + 1, h - 1], [w + 1, w - 1, w, w]):
        if 0 <= dh < H and 0 <= dw < W:
            if S[h][w] != S[dh][dw]:
                counts = dfs(dh, dw)
                black += counts[0]
                white += counts[1]
    return black, white


ans = 0
for h, w in itertools.product(range(H), range(W)):
    black, white = dfs(h, w)
    ans += black * white
print(ans)

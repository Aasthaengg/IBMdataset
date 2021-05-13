# -*- coding: utf-8 -*-
import numpy as np
from collections import deque
from collections import defaultdict
import heapq
import collections
import itertools
import bisect


mod = 10 ** 9 + 7
N, K = list(map(int, input().split()))
# N個のぼーる、K個の青いボール


def nck(n, k, mod):
    bunbo = bunshi = 1
    for i in range(k):
        bunshi = (bunshi * (n-i)) % mod
        bunbo = (bunbo * (i+1)) % mod
    return (bunshi * pow(bunbo, mod-2, mod)) % mod


ans = [0]*K
for i in range(1, K + 1):
    # i回の操作で取り除く

    # i回ってことは、i個の塊ではないとだめ
    # バラバラの場合はK個の塊がある
    # k-i個の青いボールが隣り合っている必要がある
    # print(N - K + i, i)
    # 青いボールの組の作り方
    # print("blue_set", blue_set)
    ans[i-1] = (nck(N-K+1, i, mod)*nck(K-1, i-1, mod)) % mod

for a in ans:
    print(a)

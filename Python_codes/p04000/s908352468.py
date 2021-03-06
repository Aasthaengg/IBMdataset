# -*- coding: utf-8 -*-

import sys
from collections import defaultdict, Counter

def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
sys.setrecursionlimit(10 ** 9)
INF = 10 ** 18
MOD = 10 ** 9 + 7

H, W, N = MAP()
D = defaultdict(int)

# あるマスが黒いことで黒マスが増える1〜9個の3*3正方形に+1する
for _ in range(N):
    a, b = MAP()
    for i in range(max(a-2, 1), min(a+1, H-1)):
        for j in range(max(b-2, 1), min(b+1, W-1)):
            D[(i, j)] += 1

C = Counter(D.values())
total = (H-2) * (W-2)
# 0は 全体 - 合計 で出す
print(total - sum(C.values()))
for i in range(1, 10):
    print(C[i])

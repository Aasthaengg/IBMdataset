# -*- coding: utf-8 -*-

import sys

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

N, M = MAP()

ans = list2d(M, 2, 0)
cnt = 1
for i in range(M//2):
    ans[i][0] = cnt
    cnt += 1
cnt += 1
for i in range(M//2-1, -1, -1):
    ans[i][1] = cnt
    cnt += 1
for i in range(M//2, M):
    ans[i][0] = cnt
    cnt += 1
for i in range(M-1, M//2-1, -1):
    ans[i][1] = cnt
    cnt += 1

for a, b in ans:
    print(a, b)

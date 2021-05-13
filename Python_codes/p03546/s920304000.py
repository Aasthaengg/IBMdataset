# https://atcoder.jp/contests/abc079/tasks/abc079_d

# cost[i][j] = 数字 i から数字 j に変えた時の最小コスト
# per[i][j] = 最小コストを実現した際の数字 i を数字 j に変えるのにかかるコスト
# num[i][j] = 最小コストを実現した際の新たに追加された数字 j の個数

from collections import Counter
from copy import copy

import sys
input = sys.stdin.readline

H, W = map(int, input().split())

cost = [list(map(int, input().split())) for _ in range(10)]

A = [list(map(int, input().split())) for _ in range(H)]
A = sum(A,[])

cnt = Counter(A)

for k in range(10):
    for i in range(10):
        for j in range(10):
            if cost[i][j] > cost[i][k] + cost[k][j]:
                cost[i][j] = cost[i][k] + cost[k][j]

res = 0
for i in range(10):
    res += cnt[i]*cost[i][1]


print(res)
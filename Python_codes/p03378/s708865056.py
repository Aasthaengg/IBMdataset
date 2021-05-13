# -*- coding: utf-8 -*-

N, M, X = map(int, input().split())
A = list(map(int, input().split()))

ans_l = 0 # 左に進んだ場合の答え
ans_r = 0 # 右に進んだ場合の答え

# 左に進んだ場合のコストの算出
for i in range(X, 0, -1):
    if i in A:
        ans_l += 1

# 右に進んだ場合のコストの算出
for i in range(X, N, 1):
    if i in A:
        ans_r += 1

# 最小値の算出
min_cost = min(ans_l, ans_r)

print(min_cost)
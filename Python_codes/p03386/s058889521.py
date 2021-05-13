# -*- coding: utf-8 -*-

A, B, K = map(int, input().split())

ans = []

# 以内の判定
for i in range(A, A + K):
    if i <= B:
        ans.append(i)

for j in range(B, B - K, -1):
    if j >= A:
        ans.append(j)

ans = sorted(set(ans))

for x in ans:
    print(x)
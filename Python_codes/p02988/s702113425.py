#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 問題：https://atcoder.jp/contests/abc126/tasks/abc132_b

n = int(input())
p = list(map(int, input().strip().split()))

res = 0
for i in range(n-2):
    if p[i] > p[i+1] and p[i+1] >= p[i+2]:
        res += 1
        continue
    if p[i] <= p[i+1] and p[i+1] < p[i+2]:
        res += 1
        continue

print(res)


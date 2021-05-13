#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 問題：https://atcoder.jp/contests/abc135/tasks/abc135_c

n = int(input())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))

f1 = min(a[0], b[0])
f2 = min(a[1], b[0] - f1)
res = f1 + f2
for i in range(1, n):
    f1 = min(a[i] - f2, b[i])
    f2 = min(a[i+1], b[i] - f1)
    res += f1 + f2

print(res)

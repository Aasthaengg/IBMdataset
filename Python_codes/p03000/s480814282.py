#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 問題：https://atcoder.jp/contests/abc126/tasks/abc130_b

n, x = map(int, input().strip().split())
l = list(map(int, input().strip().split()))

d = 0
i = 0
while i < n:
    d += l[i]
    if d > x:
        break
    i += 1

print(i+1)

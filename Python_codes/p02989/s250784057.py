#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 問題：https://atcoder.jp/contests/abc126/tasks/abc132_c

n = int(input())
d = list(map(int, input().strip().split()))

d = sorted(d)
res = d[n//2] - d[n//2-1]
print(res)


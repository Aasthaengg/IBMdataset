#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 問題：https://atcoder.jp/contests/abc126/tasks/abc131_b

n, l = map(int, input().strip().split())
res = n * (2 * l + n - 1) / 2
if l > 0:
    res -= l
elif l + n - 1 < 0:
    res -=  l + n - 1
print(int(res))


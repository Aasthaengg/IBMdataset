#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 問題：https://atcoder.jp/contests/abc126/tasks/abc133_c

l, r = map(int, input().strip().split())

res = 2019

if r - l >= 2019 or r % 2019 < l % 2019:
    res = 0
else:
    for i in range(l, r+1):
        for j in range(l, i):
            x = i % 2019
            y = j % 2019
            z = (x * y) % 2019
            if z < res:
                res = z

print(res)

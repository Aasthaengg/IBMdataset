#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 問題：https://atcoder.jp/contests/abc126/tasks/abc129_a

p, q, r = map(int, input().strip().split())

res = 0
if p < q:
    if q < r:
        res = p + q
    else:
        res = p + r
else:
    if p < r:
        res = p + q
    else:
        res = q + r
print(res)

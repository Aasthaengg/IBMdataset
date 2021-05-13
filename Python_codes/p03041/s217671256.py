#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 問題：https://atcoder.jp/contests/abc126/tasks/abc126_a

n, k = map(int, input().strip().split())
word = input()
res = ''

for i in range(n):
    s = word[i]
    if i == k - 1:
        s = s.lower()
    res += s

print(res)

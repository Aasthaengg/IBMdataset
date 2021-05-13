#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 問題：https://atcoder.jp/contests/abc134/tasks/abc134_c

n = int(input())
a = [int(input()) for _ in range(n)]

max_a = 0
sec_max_a = 0
for i in range(n):
    if max_a <= a[i]:
        sec_max_a = max_a
        max_a = a[i]
    elif sec_max_a < a[i]:
        sec_max_a = a[i]

for i in range(n):
    if a[i] == max_a:
        print(sec_max_a)
    else:
        print(max_a)

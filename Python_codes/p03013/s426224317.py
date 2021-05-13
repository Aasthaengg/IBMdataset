#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 問題：https://atcoder.jp/contests/abc126/tasks/abc129_c

mod = 1000000007
N, M = map(int, input().strip().split())
a = [int(input()) for _ in range(M)]
a.append(N+1)

def fibonacci(x):
    a = 1
    b = 1
    if x <= 2:
        return a
    else:
        for _ in range(x-2):
            tmp = a
            a = b
            b = tmp + b
        return b

res = 1
prev_a = -1
for cur_a in a:
    if  cur_a - prev_a == 1:
        res = 0
        break
    res *= fibonacci(cur_a - prev_a - 1) % mod
    res %= mod
    prev_a = cur_a
    continue

print(res)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 問題：https://atcoder.jp/contests/abc126/tasks/abc128_c

N, M = map(int, input().strip().split())
k = [[] for _ in range(M)]
for i in range(M):
    switches = list(map(int, input().strip().split()))
    k[i] = switches[1:]
p = list(map(int, input().strip().split()))

res = 0
for i in range(2**N):
    b = format(i, '0' + str(N) + 'b')
    can_light_up = True
    for j in range(M):
        count = 0
        for s in k[j]:
            if b[s-1] == '1':
                count += 1
        if count % 2 != p[j]:
            can_light_up = False
    if can_light_up:
        res += 1

print(res)

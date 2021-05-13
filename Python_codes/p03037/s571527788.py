#!/usr/bin/env python3
# -*- coding: utf-8 -*-

N, M = map(int, input().split())
L = []
R = []
for i in range(M):
    l, r, = map(int, input().split())
    L.append(l)
    R.append(r)
max_l = 0
min_r = N
for i in range(M):
    if max_l < L[i]:
        max_l = L[i]
    if min_r > R[i]:
        min_r = R[i]
if max_l > min_r:
    print(0)
else:
    print(min_r - max_l + 1)

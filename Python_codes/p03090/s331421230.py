#!/usr/bin/env python3
# -*- coding: utf-8 -*-

N = int(input())

phi = 0 if N & 1 else 1
print(N * (N - 1) // 2 - N // 2)
for i in range(N):
    for j in range(i+1, N):
        k, l = i+1, j+1
        if l != N - k + phi:
            print(k, l)

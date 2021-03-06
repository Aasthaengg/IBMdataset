#!/usr/bin python3
# -*- coding: utf-8 -*-

import numpy as np
n, m, q = map(int, input().split())
x = np.zeros((n,n), dtype = int)
for _ in range(m):
    l, r = map(int, input().split())
    x[r-1][l-1] += 1
x.cumsum(out = x, axis = 0)
for i in range(n):
    x[i] = np.cumsum(x[i][::-1])[::-1]

for _ in range(q):
    l, r = map(int, input().split())
    print(x[r-1][l-1])

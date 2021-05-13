#!/usr/bin/env python
# -*- coding: utf-8 -*-

n = int(input())

for i in range(n):
    x = list(map(int, input().split()))
    x.sort()
    if x[0]**2 + x[1]**2 == x[2]**2:
        print('YES')
    else:
        print('NO')
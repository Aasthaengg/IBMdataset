#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
??´?????????
"""

while True:
    inp = input().strip().split(" ")
    n = int(inp[0]) + 1
    x = int(inp[1])
    cnt = 0
    if n < 2 and x < 1:
        break
    for i in range(1, n-2):
        for j in range(i + 1, n-1):
            for k in range(j + 1, n):
                t = i + j + k
                if t == x:
                    cnt = cnt + 1
                elif t > x:
                    break
    print(cnt)
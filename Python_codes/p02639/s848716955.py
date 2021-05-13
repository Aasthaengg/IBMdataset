#!/usr/bin/env python3
# -*- coding: utf-8 -*-

x = list(map(int, input().strip().split()))
result = 0
for i in range(5):
    if x[i] == 0:
        result = i + 1
print(result)

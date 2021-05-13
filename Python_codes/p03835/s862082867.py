#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

K, S = map(int, input().strip().split())
result = 0

for x in range(K+1):
    for y in range(K+1):
        if S - x - y <= K and x + y <= S:
            result += 1

print(result)

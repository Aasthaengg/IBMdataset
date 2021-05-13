# -*- coding: utf-8 -*-
N = int(input())

import math

n = int(math.sqrt(N))
candidates = []
for i in range(1, n+1):
    if not N % i:
        if (N//i) -1 > i:
            candidates.append(N//i)


print(sum(candidates) - len(candidates))


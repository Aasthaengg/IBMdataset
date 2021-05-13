#!/usr/bin/env python3
from itertools import product

N, K = map(int, input().split())

ans = K
for i in range(N - 1):
    ans *= (K - 1)
print(ans)

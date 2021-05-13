# -*- coding: utf-8 -*-
import numpy as np

n = int(input())
a = list(map(int, input().split()))
ans = np.zeros(n, dtype=np.int)

for i in range(n):
    ans[a[i]-1] = i + 1

print(' '.join([str(i) for i in ans]))

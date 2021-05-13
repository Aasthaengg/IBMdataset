# -*- coding: utf-8 -*-
import numpy as np
def inpl(): return list(map(int, input().split()))
N, M, C = inpl()
B = np.array(inpl(), dtype=np.int64)
ans = 0
for _ in range(N):
    A = np.array(inpl(), dtype=np.int64)
    ans += np.sum(A*B)+C > 0
print(ans)

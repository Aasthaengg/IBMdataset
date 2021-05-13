#!/usr/bin/env python3
import numpy as np
import bisect
X = int(input())
A = np.cumsum(range(1, 10 ** 5))
if np.any(A == X):
    print(A.tolist().index(X) + 1)
else:
    idx = bisect.bisect_left(A, X)
    print(idx + 1)
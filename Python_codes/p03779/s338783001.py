import numpy as np
import bisect
X = int(input())
A = np.cumsum(range(1, 10 ** 5))
idx = bisect.bisect_left(A, X)
print(idx + 1)
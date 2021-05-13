import sys
readline = sys.stdin.buffer.readline

import numpy as np

n = int(readline())
a = np.array(readline().split(), np.int64)

ai = np.argsort(a)[::-1]
a = a[ai]
ai += 1

dp = np.zeros(n + 1, np.int64)
for k, (i, e) in enumerate(zip(ai, a), 1):
    dp_new = dp.copy()

    add_left = e * np.abs(np.arange(1, k + 1) - i)
    dp_new[1:k+1] = np.maximum(dp_new[1:k+1], dp[:k] + add_left)

    add_right = e * np.abs(np.arange(n - k + 1, n + 1) - i)
    dp_new[:k] = np.maximum(dp_new[:k], dp[:k] + add_right)

    dp = dp_new

ans = dp.max()
print(ans)

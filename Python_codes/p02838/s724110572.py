import sys
import numpy as np
MOD = 10**9+7

n = int(sys.stdin.buffer.readline())
a = np.fromstring(sys.stdin.buffer.readline(), dtype = np.int64, sep = ' ')
ans = 0
for i in range(60):
    s = int((a&1).sum())
    ans += s*(n-s) * 2**i
    ans %= MOD
    a >>= 1
print(ans)

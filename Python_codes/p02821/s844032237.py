import os
import sys

import numpy as np

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7
# MOD = 998244353


N, M = list(map(int, sys.stdin.buffer.readline().split()))
A = list(map(int, sys.stdin.buffer.readline().split()))

counts = np.bincount(A)
size = 1 << len(counts).bit_length() + 1
counts2 = np.rint(np.fft.irfft(np.fft.rfft(counts, size) ** 2))

cnt = 0
ans = 0
for i in np.where(counts2 > 0)[0][::-1]:
    cnt += counts2[i]
    ans += i * counts2[i]
    if cnt > M:
        ans -= i * (cnt - M)
        break
print(int(ans))

import numpy as np
import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)
fft = np.fft.rfft
ifft = np.fft.irfft
mod = 998244353

N, S = map(int, input().split())
A = list(map(int, input().split()))
U = 3003

dp = np.zeros(U+10, dtype=np.int64)
dp[0] = 1
for a in A:
    newDP = dp.copy() * 2
    newDP[a:] += dp[:-a]
    newDP %= mod
    dp = newDP

print(dp[S])
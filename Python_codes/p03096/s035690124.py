from collections import defaultdict
import sys
input = sys.stdin.buffer.readline
mod = 10**9+7

N = int(input())
dp = [0] * (N+1)
dp[0] = 1
prev = defaultdict(lambda: -1)
for i in range(1, N+1):
    c = int(input())
    dp[i] = dp[i-1]
    if prev[c] >= 0:
        if prev[c] != i-1:
            dp[i] = (dp[i] + dp[prev[c]]) % mod
    prev[c] = i

print(dp[-1])

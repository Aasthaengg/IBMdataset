import sys
N = int(input())
dp = [0] * (N + 1)
for x in map(int, sys.stdin):
    dp[x] = dp[x - 1] + 1
print(N - max(dp))
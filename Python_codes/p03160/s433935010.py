import sys

n = int(input())
a = list(map(int, input().split()))

dp = [sys.maxsize] * n
dp[0] = 0
for i in range(n):
    for j in (i + 1, i + 2):
        if j < n:
            dp[j] = min(dp[j], dp[i] + abs(a[i] - a[j]))
print(dp[n - 1], end="")

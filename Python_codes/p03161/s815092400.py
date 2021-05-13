from math import inf

n, k = map(int, input().split())
a = [int(i) for i in input().split()]
dp = [inf for _ in range(n)]
dp[0] = 0
for i in range(1, n):
    for j in range(1, k + 1):
        if i - j >= 0:
            dp[i] = min(dp[i], abs(a[i] - a[i - j]) + dp[i - j])
        else:
            break

print(dp[-1])

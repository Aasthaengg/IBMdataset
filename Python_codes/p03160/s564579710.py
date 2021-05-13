n = int(input())
h = list(map(int, input().split()))
dp = [float('inf')] * n
dp[0] = 0
dp[1] = abs(h[1]- h[0])

for i in range(2, n):
    c1 = dp[i-1] + abs(h[i] - h[i-1])
    c2 = dp[i-2] + abs(h[i] - h[i-2])
    dp[i] = c1 if c1 < c2 else c2
print(dp[n-1])
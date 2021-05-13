n = int(input())
h = list(map(int, input().split()))
INF = 10 ** 9
dp = [INF] * n
dp[0] = 0
for i in range(1, n):
    tmp = dp[i - 1] + abs(h[i] - h[i - 1])
    if dp[i] > tmp:
        dp[i] = tmp
    if i > 1:
        tmp = dp[i - 2] + abs(h[i] - h[i - 2])
        if dp[i] > tmp:
            dp[i] = tmp
print(dp[-1])

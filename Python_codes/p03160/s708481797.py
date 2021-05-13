def small(a, b):
    if a > b:
        return b
    else:
        return a


n = int(input())
h = list(map(int, input().split()))
INF = 10 ** 9
dp = [INF] * n
dp[0] = 0
for i in range(1, n):
    dp[i] = small(dp[i], dp[i - 1] + abs(h[i] - h[i - 1]))
    if i > 1:
        dp[i] = small(dp[i], dp[i - 2] + abs(h[i] - h[i - 2]))
print(dp[-1])
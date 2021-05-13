N = int(input())
h = [0] + list(map(int, input().split()))
dp = [10 ** 9] * (N + 1)
dp[1] = 0
for i in range(2, N + 1):
    if i == 2:
        dp[i] = min(dp[i], dp[i - 1] + abs(h[i] - h[i - 1]))
    else:
        dp[i] = min(dp[i], dp[i - 1] + abs(h[i] - h[i - 1]),
                    dp[i - 2] + abs(h[i] - h[i - 2]))
print(dp[-1])
# print(dp)

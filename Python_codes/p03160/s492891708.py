n = int(input())
h = list(map(int, input().split()))
dp = [10 ** 9] * n
dp[0] = 0
for i in range(1, n):
    for j in range(max(i - 2, 0), i):
        dp[i] = min(dp[i], dp[j] + abs(h[i] - h[j]))
print(dp[-1])
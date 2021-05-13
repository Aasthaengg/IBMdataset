n = int(input())
hlst = list(map(int, input().split()))
inf = 10 ** 10
dp = [inf for _ in range(n)]
dp[0] = 0
for i in range(1, n):
    dp[i] = min(dp[i - 1] + abs(hlst[i] - hlst[i - 1]), dp[i - 2] + abs(hlst[i] - hlst[i - 2]))
print(dp[-1])
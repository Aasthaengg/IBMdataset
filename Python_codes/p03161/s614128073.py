n, k = map(int, input().split())
hlst = list(map(int, input().split()))
inf = 10 ** 10
dp = [inf for _ in range(n)]
dp[0] = 0
for i in range(1, n):
    for j in range(1, k + 1):
        if i - j < 0:
            break
        dp[i] = min(dp[i - j] + abs(hlst[i] - hlst[i - j]), dp[i])
print(dp[-1])
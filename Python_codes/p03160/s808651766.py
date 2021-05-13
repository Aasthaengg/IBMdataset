INF = 10 ** 60

def li():
    return [int(x) for x in input().split()]


N = int(input())
h = li() + [INF] * 10

dp = [INF] * (N+10)

# 初期条件
dp[0] = 0
for i in range(N):
    dp[i + 1] = min(dp[i + 1], dp[i] + abs(h[i] - h[i + 1]))
    dp[i + 2] = min(dp[i + 2], dp[i] + abs(h[i] - h[i + 2]))

print(dp[N-1])
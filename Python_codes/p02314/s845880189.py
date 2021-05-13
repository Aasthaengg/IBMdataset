# 37

N, M = map(int, input().split())
C_L = [int(x) for x in input().split()]

# dp[i] = i円の支払う時のコインの最小枚数
dp = [float("Inf")] * (N+1)
dp[0] = 0
for i in range(1, N+1):
    for j in range(M):
        _c = C_L[j]
        if i >= _c:
            dp[i] = min(dp[i-_c] + 1, dp[i])

print(dp[N])


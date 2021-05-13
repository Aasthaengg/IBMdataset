N, M = map(int, input().split())
C = list(map(int, input().split()))

# dp[i][j] := C[i]までのコインを使ってj円を支払うときのコインの最小枚数
dp = [[10 ** 9] * (N+1) for _ in range(M+1)]
dp[0][0] = 0
for i in range(1,M+1):
    for j in range(N+1):
        if j - C[i-1] >= 0:
            dp[i][j] = min(dp[i][j-C[i-1]]+1, dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[M][N])


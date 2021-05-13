N, M = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
MOD = 10 ** 9 + 7
dp = [[0] * (M + 1) for i in range(N + 1)]
s = [[0] * (M + 1) for i in range(N + 1)]
dp[0][0] = 1

for i in range(N):
    for j in range(M):
        if S[i] == T[j]:
            dp[i + 1][j + 1] = s[i][j] + 1
            dp[i + 1][j + 1] %= MOD
        s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + dp[i + 1][j + 1]
        s[i + 1][j + 1] %= MOD

ans = 0
for i in range(N + 1):
    for j in range(M + 1):
        ans += dp[i][j]
        ans %= MOD
print(ans)
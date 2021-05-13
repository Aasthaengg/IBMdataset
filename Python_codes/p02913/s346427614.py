N = int(input())
S = list(input())
dp = [[0]*(N) for _ in range(N)]
for i in range(N-1):
    if S[i] == S[N-1]:
        dp[i][N-1] = 1

for i in range(N-2, -1, -1):
    for j in range(N-1, -1, -1):
        if j < i:
            if S[j] == S[i]:
                dp[j][i] = min(dp[j+1][i+1] + 1, i-j)
            else:
                dp[j][i] = 0

ans = 0
for i in range(N):
    for j in range(N):
        ans = max(ans, dp[i][j])
print(ans)
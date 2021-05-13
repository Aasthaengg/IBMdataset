N = int(input())
S = input()

dp = [[0] * N for _ in range(N)]

for j in range(N):
    if S[j] == S[-1]:
        dp[-1][j] = 1

for i in range(N - 2, -1, -1):
    for j in range(N - 1):
        if S[i] == S[j]:
            dp[i][j] = dp[i + 1][j + 1] + 1
    if S[i] == S[-1]:
        dp[i][-1] = 1

ans = 0
for i in range(N):
    for j in range(N):
        ans = max(ans, min(dp[i][j], abs(i - j)))

print(ans)

N = int(input())
S = input().strip()

dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in reversed(range(N)):
    for j in reversed(range(N)):
        if i >= j:
            continue
        if S[i] != S[j]:
            dp[i][j] = 0
        if S[i] == S[j]:
            dp[i][j] = dp[i+1][j+1] + 1

ans = 0
for i in range(N):
    for j in range(N):
        if i >= j:
            continue
        now = min([dp[i][j], j-i])
        ans = max(ans, now)

print(ans)

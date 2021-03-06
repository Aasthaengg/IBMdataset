n = int(input())
abc = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*3 for _ in range(n+1)]

for i in range(n):
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            dp[i+1][j] = max(abc[i][j]+dp[i][k], dp[i+1][j])
            dp[i+1][k] = max(abc[i][k]+dp[i][j], dp[i+1][k])

print(max(dp[-1]))
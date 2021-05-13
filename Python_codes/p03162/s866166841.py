n = int(input())
abc = [tuple(map(int,input().split())) for i in range(n)]

dp = [[0,0,0] for i in range(n+1)]


for i in range(n):
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            dp[i+1][k] = max(dp[i+1][k],dp[i][j]+abc[i][k])

print(max(dp[-1]))
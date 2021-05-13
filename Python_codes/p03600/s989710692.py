n = int(input())
dp = [list(map(int,input().split())) for _ in range(n)]
ans = sum([sum(i) for i in dp])
for i in range(n):
    for j in range(n):
        if dp[i][j] == 0:continue
        a = 0
        for k in range(n):
            if dp[i][k] == 0:continue
            if j == k:continue
            if dp[i][k]+dp[k][j] < dp[i][j]:print(-1);exit()
            if dp[i][k] + dp[k][j] == dp[i][j]:
                a = 1
        if a == 1:ans -= dp[i][j]
print(ans//2)
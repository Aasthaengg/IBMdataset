# 63


n = int(input())
dp = [[int(x) for x in input().split()] for y in range(n)]
del_l = []
ans = 0

for i in range(n-1):
    for j in range(i+1,n):
        for k in range(n):
            if k in (i,j):
                continue
            if dp[i][j] > dp[i][k] + dp[k][j]:
                print("-1")
                exit()
            elif dp[i][j] == dp[i][k] + dp[k][j]:
                break
        else:
            ans += dp[i][j]

print(ans)
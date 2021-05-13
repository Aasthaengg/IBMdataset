n = int(input())
p = [float(i) for i in input().split()]
#i枚目までのコインでj枚表が出ている確率
dp = [[0] * i for i in range(2,n+2)]

dp[0][1] = p[0]
dp[0][0] = 1-p[0]
ans = 0
if n != 1:
    for i in range(1,n):
        for j in range(len(dp[i])-1):
            #i枚目で裏が出る確率
            dp[i][j] += dp[i-1][j] * (1-p[i])
            #i枚目で表が出る確率
            dp[i][j+1] += dp[i-1][j] * p[i]
    for i in range(1,(n+1)//2+1):
        ans += dp[n-1][-i]
    print(ans)
else:
    print(p[0])

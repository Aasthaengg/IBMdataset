N=int(input())
p=list(map(float,input().split()))

#i枚投げて，j枚が表である確率
dp=[[0]*(N+1) for _ in range(N+1)]

dp[0][0]=1

for i in range(N):
    for j in range(N):
        dp[i+1][j]+=dp[i][j]*(1-p[i])
        dp[i+1][j+1]+=dp[i][j]*p[i]
        if j==i:
            break
            
print(1.0-sum(dp[-1][:N//2+1]))



x=int(input())

dp=[[0]*(x+1) for _ in range(7)]
dp[0][0]=1
price=list(range(100,106))

for i in range(6):
    p=price[i]
    for j in range(x+1):
        dp[i+1][j]=dp[i][j]

        if j>=p:
            dp[i+1][j]+=dp[i+1][j-p]

print(1 if dp[6][x] else 0)
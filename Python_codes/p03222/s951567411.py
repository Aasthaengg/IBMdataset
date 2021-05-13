h,w,k=map(int,input().split())
mod=10**9+7
dp=[[0]*w for i in range(h+1)]
dp[0][0]=1
data=[]
for i in range(2**(w-1)):
    for j in range(1,w-1):
        if (i>>j)&1==(i>>j-1)&1 and (i>>j)&1==1:
            break
    else:
        data.append(i)
for i in range(1,h+1):
    for u in data:
        if u&1==1:
            dp[i][0]=(dp[i][0]+dp[i-1][1])%mod
        else:
            dp[i][0]=(dp[i][0]+dp[i-1][0])%mod
        if w>1:
            if (u>>w-2)&1==1:
                dp[i][w-1]=(dp[i][w-1]+dp[i-1][w-2])%mod
            else:
                dp[i][w-1]=(dp[i][w-1]+dp[i-1][w-1])%mod
        for j in range(1,w-1):
            if (u>>j-1)&1==1:
                dp[i][j]=(dp[i][j]+dp[i-1][j-1])%mod
            elif (u>>j)&1==1:
                dp[i][j]=(dp[i][j]+dp[i-1][j+1])%mod
            else:
                dp[i][j]=(dp[i][j]+dp[i-1][j])%mod
print(dp[h][k-1])  
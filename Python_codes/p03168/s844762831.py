n=int(input())
p=list(map(float,input().split()))

dp=[[0]*(n+1) for i in range(n)]

for i in range(n):
    for j in range(n+1):

        if i==0:
            dp[0][0]=1-p[i]
            dp[0][1]=p[i]
        else:
            #表が出る
            if dp[i-1][j-1]!=0:
                dp[i][j]+=dp[i-1][j-1]*p[i]
            #裏
                dp[i][j-1]+=dp[i-1][j-1]*(1-p[i])

print(sum(dp[-1][int(n/2)+1:]))
#print(dp)

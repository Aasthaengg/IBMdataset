n,t= map(int, input().split())
a= list(map(int, input().split()))

# dp[i][0]:０からiまでの区間に置けるMIN
# dp[i][1]:その区間での左から右への差の最大値
# dp[i][2]:最大値をとるものがいくつあるか
dp=[[float('inf'),0,0] for i in range(n)]

for i in range(n):
    if i==0:
        dp[i][0]=a[i]
    else:
        dp[i][0]=min(dp[i-1][0],a[i])
        if dp[i-1][1]<a[i]-dp[i-1][0]:
            dp[i][1]=a[i]-dp[i-1][0]
            dp[i][2]=1
        elif dp[i-1][1]==a[i]-dp[i-1][0]:
            dp[i][1]=dp[i-1][1]
            dp[i][2]=dp[i-1][2]+1
        else:
            dp[i][1]=dp[i-1][1]
            dp[i][2]=dp[i-1][2]


print(dp[-1][2])
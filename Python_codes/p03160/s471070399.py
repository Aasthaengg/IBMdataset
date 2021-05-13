INT_MAX= 100000000
n=int(input())
dp  = [INT_MAX]*(100001)
h=[int(X) for X in input().split()]
dp[0]=0
dp[1]=abs(h[1]-h[0])
for i in range(2,n):

    dp[i]=min(dp[i-1]+abs(h[i]-h[i-1]),dp[i-2]+abs(h[i-2]-h[i]))

print(dp[n-1])
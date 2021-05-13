import sys
n,k=map(int,input().split())
h=list(map(int,input().split()))
dp=[sys.maxsize]*n
dp[0]=0
for i in range(1,n):
    for j in range(1,min(k+1,i+1)):
            dp[i]=min(abs(h[i-j]-h[i])+dp[i-j],dp[i])


print(dp[-1])

import sys
n=int(input())
dp=[0]*(n+1)
dp[0]=1
s=0
for i in range(3,n+1):
    s+=dp[i-3]
    s=s%1000000007
    dp[i]=s
dp[0]=0
print(dp[n])
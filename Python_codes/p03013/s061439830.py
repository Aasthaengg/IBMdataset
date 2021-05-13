import sys
input=sys.stdin.readline
n,m=map(int,input().split())
if m>0:
    a=[int(input()) for i in range(m)]

dp=[None]*(n+1)
dp[0]=1
for i in range(m):
    dp[a[i]]=0
if dp[1]==None:
    dp[1]=1

for i in range(2,n+1):
    if dp[i]==None:
        dp[i]=(dp[i-2]+dp[i-1])%1000000007

print(dp[-1])
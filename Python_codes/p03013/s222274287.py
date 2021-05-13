import sys
n,m=map(int,input().split())
if m != 0:
  a=set(map(int,sys.stdin.read().split()))
else:
  a=set()

modx=10**9+7

dp=[0]*(n+10)
dp[0]=1

for i in range(n+1):
  if i+1 not in a:
    dp[i+1]= (dp[i]+dp[i+1]) % modx
  if i+2 not in a:
    dp[i+2]= (dp[i]+dp[i+2]) % modx

print(dp[n])
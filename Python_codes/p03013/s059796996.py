from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

n,m=nii()

mod=10**9+7

dp=[-1 for i in range(n+1)]
dp[0]=1
dp[1]=1
for i in range(m):
  a=int(input())
  dp[a]=0

for i in range(2,n+1):
  if dp[i]==0:
    continue
  num=dp[i-2]+dp[i-1]
  num%=mod
  dp[i]=num

print(dp[-1])
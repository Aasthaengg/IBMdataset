MOD=10**9+7
n,m=map(int,input().split())
a=set([int(input()) for _ in range(m)])
dp=[0]*(n+1)
if n==1:
  print(1)
  exit()
if 1 in a and 2 in a:
  print(0)
  exit()
elif 1 in a:
  dp[1]=0
  dp[2]=1
elif 2 in a:
  dp[1]=1
  dp[2]=0
else:
  dp[1]=1
  dp[2]=2
  
for i in range(3,n+1):
  if i in a:
    dp[i]=0
  else:
    dp[i]=(dp[i-1]+dp[i-2])%MOD
print(dp[-1]%MOD)
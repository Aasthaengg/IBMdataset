n,m=map(int,input().split())
a=[0]*(n)
if n==1:
  print(1)
  exit()
if m>0:
  for _ in range(m):
    a[int(input())]+=1
dp=[0]*(n+1)
dp[0]=1
if a[1]!=1:
  dp[1]=1
for i in range(2,n+1):
  if a[i-2]==0 and a[i-1]==0:
    dp[i]=dp[i-2]+dp[i-1]
  elif a[i-1]!=0 and a[i-2]==0:
    dp[i]=dp[i-2]
  elif a[i-2]!=0 and a[i-1]==0:
    dp[i]=dp[i-1]
  else:
    dp[i]=0
print(dp[n]%(10**9+7))    

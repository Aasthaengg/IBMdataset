n,k=map(int,input().split())
h=list(map(int,input().split()))
dp=[10**10]*n
for i in range(n):
  if i==0:
    dp[i]=0
  elif i==1:
    dp[i]=abs(h[1]-h[0])
  else:
    for j in range(1,min(i,k)+1):
      dp[i]=min(dp[i],dp[i-j]+abs(h[i]-h[i-j]))
print(dp[-1])
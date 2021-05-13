n,k,*a=map(int,open(0).read().split())
dp=[0]*-~k
for i,d in enumerate(dp):
  if d:continue
  for j in a:
    if i+j<=k:
      dp[i+j]=1
print('SFeicrosntd'[dp[k]::2])
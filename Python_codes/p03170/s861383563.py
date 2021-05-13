n,k=map(int,input().split())
arr=list(map(int,input().split()))
dp=[False]*(2*k+1)
for i in range(k):
  for val in arr:
    if dp[i]==False:
      dp[i+val]=True
if dp[k]==True:
  print('First')
else:
  print('Second')
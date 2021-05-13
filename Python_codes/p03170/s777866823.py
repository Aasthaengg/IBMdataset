n,k=map(int,input().split())
a=list(map(int,input().split()))
dp=[False]*(k+1)
for i in range(1,k+1):
  for j in range(n):
    if  i-a[j]<0:
      break
    if dp[i-a[j]]==False:
      dp[i]=True
if dp[k]==True:
  print('First')
else:
  print('Second')

          

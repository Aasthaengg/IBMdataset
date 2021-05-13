n,k=map(int,input().split())
li=[int(k) for k in input().split()]
dp=[False]*(k+1)
for i in range(1,k+1):
  for j in range(len(li)):
    if i-li[j]<0:
      continue
    if dp[i-li[j]]==False:
      dp[i]=True
      break
if dp[k]==True:
  print("First")
else:
  print("Second")
  
  

n=int(input())
money=[1]
dp=[0]*(n+1)
dp[1]=1
m=6
i=1
while m<=n:
  money.append(m)
  i+=1
  m=6**i
m=9
i=1
while m<=n:
  money.append(m)
  i+=1
  m=9**i

for m in money:
  dp[m]=1

money.sort()
for i in range(1,n+1):
  for m in money:
    if i+m>=n+1:
      continue
    if dp[i]+1<=dp[i+m] or dp[i+m]==0:
      dp[i+m]=dp[i]+1
      
print(dp[n])
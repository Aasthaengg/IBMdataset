n,k=map(int,input().split())
a=list(map(int,input().split()))
dp=[False]*(k+1)
for i in range(1,k+1):
  for j in range(n):
    if i-a[j]>=0:
      dp[i] |= not(dp[i-a[j]])
#print(dp)
print("First" if dp[k] else "Second")
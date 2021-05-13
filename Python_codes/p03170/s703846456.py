n,k=map(int,input().split())
A=list(map(int,input().split()))
dp=[0]*(2*k)
for i in range(k+1):
  a=0
  for j in range(n):
    if dp[i-A[j]]==1:
      a=1
  if a==0:
    dp[i]=1
if dp[k]==0:
  print("First")
else:
  print("Second")
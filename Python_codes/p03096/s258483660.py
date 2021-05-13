n=int(input())
arr=[int(input()) for _ in range(n)]
mod=10**9+7

dp=[0]*n
dp[0]=1

record={arr[0]:0}

for i,v in enumerate(arr):
  if i==0:
    continue
  dp[i]=dp[i-1]
  if v in record and record[v]<i-1:
    dp[i]+=dp[record[v]]
    dp[i]=dp[i]%mod
  record[v]=i
print(dp[-1])

n,m=map(int, input().split())
a=set(int(input())  for i in  range(m))
x=(10**9)+7

dp=[0]*(n+1)
dp[0]=1
if 1 not in a:
  dp[1]=1

for i in range(2,n+1):
  if i in a:
    continue
  dp[i]+=dp[i-1]+dp[i-2]
  #print(dp)
  
print(dp[-1]%x)
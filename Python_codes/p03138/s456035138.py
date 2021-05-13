n,k=map(int,input().split())
a=list(map(int,input().split()))

lst=[0]*50


for i in a:
  for j in range(50):
    if (i>>j)%2==1:
      lst[j]+=1

k=bin(k)[2:]

dp=[[0]*2 for i in range(len(k)+1)]


for i in range(len(k)):
  if k[i]=='1':
    dp[i+1][0]=dp[i][0]+(n-lst[len(k)-i-1]*2)*(2**(len(k)-i-1))
    dp[i+1][1]=dp[i][0]
  else:
    dp[i+1][0]=dp[i][0]

  if i==0:
      continue
  
  dp[i+1][1]=max(dp[i+1][1],dp[i][1],dp[i][1]+(n-lst[len(k)-i-1]*2)*(2**(len(k)-i-1)))


print(sum(a)+max(dp[-1][0],dp[-1][1]))
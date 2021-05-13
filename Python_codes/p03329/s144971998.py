n=int(input())
dp=[None]*(n+1)
dp[0]=0

a=1

lst=[]

while a<=n:
  dp[a]=1
  lst+=[a]
  a*=6

a=1

while a<=n:
  dp[a]=1
  lst+=[a]
  a*=9

for i in range(n):
  if dp[i]!=None:
    for j in lst:
      if i+j<=n:
        if dp[i+j]!=None:
          dp[i+j]=min(dp[i+j],dp[i]+1)
        else:
          dp[i+j]=dp[i]+1

print(dp[n])
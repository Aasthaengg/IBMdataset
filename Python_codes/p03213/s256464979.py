import math
n=int(input())
p=[0]*101
dp=[0]*101
for i in range(2,n+1):
  for j in range(2,i+1):
    while i%j==0:
      i//=j
      p[j]+=1
for i in range(101):
  if p[i]!=0:
    dp[p[i]]+=1
ans=sum(dp[74:])+sum(dp[24:])*(sum(dp[2:])-1)+sum(dp[14:])*(sum(dp[4:])-1)+sum(dp[4:])*(sum(dp[4:])-1)//2*(sum(dp[2:])-2)
print(ans)
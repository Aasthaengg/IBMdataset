N=int(input())
dp=[0]*9
a=list(map(int,input().split()))
for i in range(N):
  if a[i]>=3200:
    a[i]=3200
  dp[a[i]//400]+=1
s=0
for i in range(8):
  if dp[i]==0:
    s+=1
b=sum(dp[8:])
if s==8:
  print(1,b)
else:
  print(8-s,8-s+b)
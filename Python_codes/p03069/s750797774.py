from itertools import *
n=int(input())
s=input()
w=[0]*(n+1)
b=[0]*(n+1)
for i,j in enumerate(s):
  if j=='.':w[i]=1
  else:b[i+1]=1
for i in range(n):
  w[n-i-1]+=w[n-i]
  b[i+1]+=b[i]
ans=10**18
for i,j in zip(w,b):
  ans=min(ans,i+j)
print(ans)
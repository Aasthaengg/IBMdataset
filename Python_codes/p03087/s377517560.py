n,q=map(int,input().split())
s=input()
c=[0]*n
for i in range(1,n):
  t=s[i-1:i+1]
  if t=="AC":c[i]+=1
from itertools import accumulate
s=list(accumulate(c))
for i in range(q):
  l,r=map(int,input().split())
  l-=1
  r-=1
  print(s[r]-s[l])



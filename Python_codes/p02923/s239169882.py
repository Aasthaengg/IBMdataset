n=int(input())
h=list(map(int,input().split()))
from itertools import groupby
t=[]
for i in range(1,n):
  if h[i]-h[i-1]<=0:t.append(1)
  else:t.append(0)
gr=groupby(t)
ans=0
for k,g in gr:
  if k==1:
    t=len(list(g))
    ans=max(ans,t)
print(ans)


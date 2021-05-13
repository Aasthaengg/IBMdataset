q=int(input())
n=10**5+10
d=[0]+[1 for _ in range(n)]

d[1]=0
f=2
while f*f<n+1:
  i=2
  while f*i<=n:
    d[f*i]=0
    i+=1
  f+=1
  while d[f]==0 and f*f<n+1:
    f+=1

e=[0 for _ in range(n+1)]
for i in range(1,n+1,2):
  if d[i]==1 and d[(i+1)//2]==1:
    e[i]=1

e[1]=0

import itertools
an=list(itertools.accumulate(e))

for i in range(q):
  l,r=map(int,input().split())
  print(an[r]-an[l-1])
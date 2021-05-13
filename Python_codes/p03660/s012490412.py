import sys
from collections import defaultdict
from collections import deque

n=int(input())
edges=[tuple(map(int,input().split())) for _ in range(n-1)]
d=defaultdict(list)
for e in edges:
  d[e[0]].append(e[1])
  d[e[1]].append(e[0])
fnc=[-1]*(n+1)
snk=[-1]*(n+1)
fnc[1]=0
snk[n]=0
cv=deque([1])
nv=deque([1])
c=-1
while nv:
  c+=1
  cv.extend(nv)
  nv.clear()
  for e in cv:
    fnc[e]=c
    for x in d[e]:
      if fnc[x]<0:
        nv.append(x)
  cv.clear()
cv.append(n)
nv=deque([1])
c=-1
while nv:
  c+=1
  cv.extend(nv)
  nv.clear()
  for e in cv:
    snk[e]=c
    for x in d[e]:
      if snk[x]<0:
        nv.append(x)
  cv.clear()

j=sum([(fnc[i]<=snk[i])-(fnc[i]>snk[i]) for i in range(1,n+1)])
if j>0:
  print('Fennec')
else:
  print('Snuke')
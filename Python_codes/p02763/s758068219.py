n=int(input())
s=[*input()]
q=int(input())
from collections import *
d=defaultdict(list)
for i,c in enumerate(s):
  d[c]+=[i]
from bisect import *
for _ in range(q):
  x,y,z=input().split()
  y=int(y)-1
  if x=='1':
    if s[y]==z: continue
    d[s[y]].pop(bisect(d[s[y]],y)-1)
    s[y]=z
    insort(d[z],y)
  else:
    print(sum(bisect(l,int(z)-1)-bisect_left(l,y)>0 for l in d.values()))
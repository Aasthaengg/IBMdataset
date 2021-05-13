from collections import defaultdict as dd
from itertools import accumulate as ac
from itertools import product as pr

N,W=map(int,input().split())
d=dd(list)
for _ in range(N):
  w,v=map(int,input().split())
  d[w].extend([v])
d=dict(d)
for i in d.keys():
  d[i].sort(reverse=True)
  d[i]=[0]+list(ac(d[i]))

l=[]
key=list(d.keys())
for val in pr(*map(enumerate,d.values())):
  weight=sum(map(lambda x,y:x*y[0],key,val))
  value=sum(map(lambda x:x[1],val))
  if weight<=W:
    l.extend([value])

print(max(l))
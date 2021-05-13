n=int(input())
from collections import deque
d=deque(['a'])
c=[chr(i) for i in range(97, 97+26)]
ans=set([])
while d:
  y=d.pop()
  if len(y)==n:
    ans.add(y)
  now=c.index(sorted(y)[-1])
  for z in range(min(now+2,n+1)):
    if z>-1 and len(y)<n:
      d.append(y+c[z])
for z in sorted(list(ans)):
  print(z)
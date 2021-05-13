import sys
from collections import deque
s=sys.stdin.readlines()
_,q=map(int,s[0].split())
f=lambda x,y:(x,int(y))
d=deque(f(*e.split())for e in s[1:])
t=0
while d:
 k,v=d.popleft()
 if v>q:
  v-=q
  t+=q
  d.append([k,v])
 else:
  t+=v
  print(k,t)

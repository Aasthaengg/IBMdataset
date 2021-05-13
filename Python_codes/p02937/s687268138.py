import sys
import heapq
import bisect
from collections import deque
stdin=sys.stdin

ns=lambda:input().rstrip()
ni=lambda:int(input().rstrip())
nm=lambda:map(int,input().split())
nl=lambda:list(map(int,input().split()))

s=list(ns())
t=list(ns())
d={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}

order=[[] for _ in range(26)]

for i in range(len(s)):
  order[d[s[i]]].append(i)
  
now=0
ans=0
rep=0
for i in range(len(t)):
  inds=d[t[i]]
  if(order[inds]==[]):
    print(-1)
    sys.exit(0)
  index=bisect.bisect_left(order[inds],now)
  if(index==len(order[inds])):
    now=order[inds][0]+1
    rep+=1
  else:
    now=order[inds][index]+1


print(rep*len(s)+now)
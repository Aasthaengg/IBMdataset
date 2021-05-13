import math
import sys
from collections import deque
import copy
import itertools
from itertools import permutations
def mi() : return map(int,sys.stdin.readline().split())
def ii() : return int(sys.stdin.readline().rstrip())
a,b=mi()
l=[list(mi()) for _ in range(b)]
l=sorted(l,key=lambda x:x[1])
q=deque([1,1])
ans=0
for i,j in l:
  y=q.pop()
  x=q.pop()
  if i<x:
    q.append(x)
    q.append(y)
  else:
    ans+=1
    q.append(j)
    q.append(j)
print(ans)

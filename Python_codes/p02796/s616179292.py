import math
import sys
from collections import deque
import copy
import itertools
from itertools import permutations
def mi() : return map(int,sys.stdin.readline().split())
def ii() : return int(sys.stdin.readline().rstrip())
def i() : return sys.stdin.readline().rstrip()
a=ii()
List=[]
for i in range(a):
  u,v=mi()
  List.append([u-v,u+v])
List=sorted(List , key=lambda x:x[1])
q=deque([List[0][1]])
ans=1
for i,j in List:
  u=q.pop()
  if u<=i:
    q.append(j)
    ans+=1
  else:
    q.append(u)
print(ans)
import math
import sys
from collections import deque
import copy
def mi() : return map(int,input().split())
a,b=mi()
l=[list(input()) for _ in range(a)]
count=0
for i in range(a):
  for _ in range(b):
    if l[i][_]==".":
      count+=1
l[0][0]=1
q=deque([[0,0]])
while q:
  x,y=q.popleft()
  if x==a-1 and y==b-1:
    print(count-l[x][y])
    sys.exit()
  for e,f in [[0,1],[0,-1],[1,0],[-1,0]]:
    if 0<=x+e<a and 0<=y+f<b and l[x+e][f+y]==".":
      l[x+e][f+y]=l[x][y]+1
      q.append([x+e,y+f])
print(-1)
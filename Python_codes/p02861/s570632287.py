n=int(input())
l=[]

for i in range(n):
  x,y=map(int,input().split())
  l.append([x,y])

import itertools

seq=[i for i in range(n)]
p=list(itertools.permutations(seq))
import math

ans=0
for pp in p:
  for i in range(n-1):
    xy=math.sqrt((l[pp[i]][0]-l[pp[i+1]][0])**2 + (l[pp[i]][1]-l[pp[i+1]][1])**2)
    ans+=xy

print(ans/len(p))
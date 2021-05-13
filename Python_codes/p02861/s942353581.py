from math import sqrt
from itertools import permutations
N=int(input())
xy=[list(map(int,input().split())) for _ in range(N)]
ans=0
cnt=0
for i in permutations(range(N)):
  d=0
  for j in range(N-1):
    dx=xy[i[j+1]][0]-xy[i[j]][0]
    dy=xy[i[j+1]][1]-xy[i[j]][1]
    d+=sqrt(dx**2+dy**2)
  ans+=d
  cnt+=1
print(ans/cnt)
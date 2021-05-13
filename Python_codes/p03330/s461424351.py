n,nc=map(int,input().split())
d=[list(map(int,input().split())) for _ in range(nc)]
c=[list(map(int,input().split())) for _ in range(n)]
from collections import defaultdict
dct=defaultdict(int)
for x in range(n):
  for y in range(n):
    for ci in range(nc):
      if (ci,(x+y)%3) in dct:
        dct[(ci,(x+y)%3)]+=d[c[x][y]-1][ci]
      else:
        dct[(ci,(x+y)%3)]=d[c[x][y]-1][ci]

def func(c1,c2,c3): #(i+j)%=0をc1に、=1をc2に、=2をc3に塗るときの違和感
  ret=dct[(c1,0)]+dct[(c2,1)]+dct[(c3,2)]
  return ret
ans=float('inf')
for c1 in range(nc):
  for c2 in range(nc):
    if c1==c2:continue
    for c3 in range(nc):
      if c1==c3 or c2==c3:continue
      ans=min(ans,func(c1,c2,c3))
print(ans)
#print(dct)
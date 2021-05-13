n,k=map(int,input().split())
xy=[list(map(int,input().split())) for _ in range(n)]
# 座圧
x,y=zip(*xy)
xsort=list(x)
ysort=list(y)
xsort.sort()
ysort.sort()
from bisect import bisect_left
x=[bisect_left(xsort,xi) for xi in x]
y=[bisect_left(ysort,yi) for yi in y]
xy=list(zip(x,y))
pmap=[[0]*(n) for _ in range(n)]
for x,y in xy:
  pmap[x][y]+=1
#print(pmap)
for i in range(n):
  tmp=0
  for j in range(n):
    tmp+=pmap[i][j]
    pmap[i][j]=tmp
    if i!=0:
      pmap[i][j]+=pmap[i-1][j]
def func(x1,y1,x2,y2):
  if x1==x2 or y1==y2:return 0
  if x1>x2:x1,x2=x2,x1
  if y1>y2:y1,y2=y2,y1
  if x1==0 and y1==0:
    return pmap[x2][y2]
  elif x1==0:
    return pmap[x2][y2]-pmap[x2][y1-1]
  elif y1==0:
    return pmap[x2][y2]-pmap[x1-1][y2]
  else:
    return pmap[x2][y2]-pmap[x1-1][y2]-pmap[x2][y1-1]+pmap[x1-1][y1-1]

ans=float('inf')
for x1 in range(n-1):
  for x2 in range(x1+1,n):
    for y1 in range(n-1):
      for y2 in range(1,n):
        c=func(x1,y1,x2,y2)
        if func(x1,y1,x2,y2)>=k:
          #print(xsort[x1],xsort[x2],xsort[y1],xsort[y2])
          b=abs(xsort[x1]-xsort[x2])*abs(ysort[y1]-ysort[y2])
          ans=min(ans,b)
print(ans)
#print(pmap)
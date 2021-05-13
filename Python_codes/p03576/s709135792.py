def check(x1,x2,y1,y2):
  p1=x1
  p2=x2
  q1=y1
  q2=y2
  if x1<=x2:
    x1=p1
    x2=p2
  else:
    x1=p2
    x2=p1
  if y1<=y2:
    y1=q1
    y2=q2
  else:
    y1=q2
    y2=q1
  count=0
  for ttx,tty in xy:
    if x1<=ttx<=x2 and y1<=tty<=y2:
      count+=1
  if count>=k:
    res=True
  else:
    res=False
  return res

n,k=map(int,input().split())
x,y=[],[]
xy=[]
for i in range(n):
  a,b=map(int,input().split())
  x.append(a)
  y.append(b)
  xy.append((a,b))
from itertools import combinations
ans=10**20
for xx in combinations(x,2):
  for yy in combinations(y,2):
    if check(xx[0],xx[1],yy[0],yy[1]):
      tmp=abs(xx[0]-xx[1])*abs(yy[0]-yy[1])
      ans=min(ans,tmp)
print(ans)
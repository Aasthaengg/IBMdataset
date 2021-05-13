w,h,n=map(int,input().split())
minx,maxx=0,w
miny,maxy=0,h

for i in range(n):
  x,y,a=map(int,input().split())
  if a==1:
    minx=max(minx,x)
  if a==2:
    maxx=min(maxx,x)
  if a==3:
    miny=max(miny,y)
  if a==4:
    maxy=min(maxy,y)
xx=(maxx-minx)
yy=(maxy-miny)
if xx>0 and yy>0:
  print(xx*yy)
else:
  print(0)
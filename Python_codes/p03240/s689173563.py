n=int(input())
xyh=[list(map(int,input().split()))[::-1]for _ in range(n)]
xyh.sort(reverse=1)
for xx in range(101):
  for yy in range(101):
    f=True
    hh=xyh[0][0]+abs(xx-xyh[0][2])+abs(yy-xyh[0][1])
    for h,y,x in xyh[1:]:
      if max(hh-abs(x-xx)-abs(y-yy),0)!=h:f=False
    if f:print(xx,yy,hh);exit()
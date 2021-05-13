n=int(input())
xyh=[list(map(int,input().split())) for _ in range(n)]
x0,y0,h0=0,0,0
for x,y,h in xyh:
  if h>0:
    x0,y0,h0=x,y,h
    break
# 頂点を固定して全探索
for cx in range(101):
  for cy in range(101):
    h=h0+abs(cx-x0)+abs(cy-y0)
    flg=True
    for xi,yi,hi in xyh:
      if hi!=max(h-abs(cx-xi)-abs(cy-yi),0):
        flg=False
    if flg:
      print(cx,cy,h)

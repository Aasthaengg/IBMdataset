w,h,n = map(int, input().split())
x1,x2,y1,y2 = 0,w,0,h
for _ in range(n):
  xi,yi,ai = map(int, input().split())
  if ai==1: x1 = max(xi,x1)
  elif ai==2: x2 = min(xi,x2)
  elif ai==3: y1 = max(yi,y1)
  else: y2 = min(yi,y2)
dx = max(0, x2-x1)
dy = max(0, y2-y1)
print(dx*dy)
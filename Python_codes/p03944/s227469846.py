w,h,n=map(int,input().split())
x1,x2,y1,y2=0,w,0,h
for i in range(n):
  x,y,a=map(int,input().split())
  if a==1 and x > x1:
    x1 = x
  elif a==2 and x < x2:
    x2 = x
  elif a==3 and y > y1:
    y1 = y
  elif a==4 and y < y2:
    y2 = y
if x1 > x2 or y1 > y2:
  print(0)
else:
  print((x2 - x1)*(y2 - y1))
w,h,n=map(int,input().split())

y_max,x_max=h,w
y_min,x_min=0,0

for i in range(n):
  x,y,a=map(int,input().split())
  if a==1:
    x_min=max(x_min,x)
  elif a==2:
    x_max=min(x_max,x)
  elif a==3:
    y_min=max(y_min,y)
  elif a==4:
    y_max=min(y_max,y)

width=max(x_max-x_min,0)
height=max(y_max-y_min,0)

print(int(width*height))




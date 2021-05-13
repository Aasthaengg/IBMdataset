x1,y1,x2,y2=map(int,input().split())
x=abs(x2-x1)
y=abs(y2-y1)
if x2>x1:
  if y2>y1:
    print(x2-y,y2+x,x1-y,y1+x)
  else:
    print(x2+y,y2+x,x1+y,y1+x)
else:
  if y2>y1:
    print(x2-y,y2-x,x1-y,y1-x)
  else:
    print(x2+y,y2-x,x1+y,y1-x)
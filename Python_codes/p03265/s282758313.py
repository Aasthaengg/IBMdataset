x1,y1,x2,y2=map(int,input().split())
if x2 >= x1 and y2 >= y1:
  x3=x2-abs(y2-y1)
  x4=x1-abs(y2-y1)
  y3=y2+abs(x2-x1)
  y4=y1+abs(x2-x1)
elif x2 < x1 and y2 >= y1:
  x3=x2-abs(y2-y1)
  x4=x1-abs(y2-y1)
  y3=y2-abs(x2-x1)
  y4=y1-abs(x2-x1)
elif x2 < x1 and y1 >= y2:
  x3=x2+abs(y2-y1)
  x4=x1+abs(y2-y1)
  y3=y2-abs(x2-x1)
  y4=y1-abs(x2-x1)
else:
  x3=x2+abs(y2-y1)
  x4=x1+abs(y2-y1)
  y3=y2+abs(x2-x1)
  y4=y1+abs(x2-x1)
print(x3,y3,x4,y4)
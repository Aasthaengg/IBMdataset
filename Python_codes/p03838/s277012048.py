x,y=map(int,input().split())
if x>0:
  if y>x:
    print(y-x)
  elif 0<y<x:
    print(x-y+2)
  elif y<=0:
    print(abs(abs(x)-abs(y))+1)
elif x==0:
  if y>0:
    print(y-x)
  else:
    print(x-y+1)
else:
  if y<x:
    print(x-y+2)
  elif x<y<=0:
    print(y-x)
  else:
    print(abs(abs(x)-abs(y))+1)
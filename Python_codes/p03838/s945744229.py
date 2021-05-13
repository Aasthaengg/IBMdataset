x,y=map(int,input().split())
if x==0:
  a=abs(y-x)
  if y<0:
    print(a+1)
  else:
    print(a)
  exit()
if y==0:
  a=abs(x-y)
  if x<=0:
    print(a)
  else:
    print(a+1)
  exit()
if x>0:
  if abs(y)>=x:
    a=abs(y)-x
    if y<0:
      print(a+1)
    else:
      print(a)
  else:
    a=x-abs(y)
    if y<0:
      print(a+1)
    else:
      print(a+2)
  exit()
#x<0
if abs(y)>abs(x):
  a=abs(y)-abs(x)
  if y>0:
    print(a+1)
  else:
    print(a+2)
else:
  a=abs(abs(y)-abs(x))
  if y<0:
    print(a)
  else:
    print(a+1)
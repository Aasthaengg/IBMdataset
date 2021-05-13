x,y=map(int,input().split())
a=abs(abs(x)-abs(y))
if x==0:
  if y<0:
    print(a+1)
  else:
    print(a)
elif y==0:
  if x<0:
    print(a)
  else:
    print(a+1)
elif y*x>0 and y>x:
  print(a)
elif y*x>0 and x>y:
  print(a+2)
elif y*x<0:
  print(a+1)

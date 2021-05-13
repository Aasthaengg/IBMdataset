x,y = map(int,input().split())

if ((x<0)and(y==0)) or ((x == 0)and(y>=0)):
  print(abs(abs(x)-abs(y)))
elif ((x==0)and(y<0))or((x>0)and(y==0)):
  print(abs(abs(x)-abs(y))+1)
elif ((x>0)and(y>0))or((x<0)and(y<0)):
  if x>y:
    print(abs(abs(x)-abs(y))+2)
  elif x == y:
    print(0)
  else:
    print(abs(abs(x)-abs(y)))
else:
  if (-1*x)>y:
    print(abs(abs(x)-abs(y))+1)
  elif (-1*x) == y:
    print(1)
  else:
    print(abs(abs(x)-abs(y))+1)
x,y=map(int,input().split())
if x==0:
  if y<0:
    print(-1*y+1)
  else:
    print(y)
    
elif x>0:
  if -1*x<y<x:
    if y<=0:
      print(y+x+1)
    else:
      print(x-y+2)
  elif x<y:
    print(y-x)
  else:
    print(-1*y-x+1)
    
else:
  if x<y<-1*x:
    if y<=0:
      print(y-x)
    else:
      print(-1*y-x+1)
  elif y<x:
    print(-1*y+x+2)
  else:
    print(y+x+1)

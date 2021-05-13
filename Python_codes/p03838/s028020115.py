import numpy as np
x,y = map(int,input().split())
if abs(x)<abs(y):
  if x<0 and y<0:
    print(abs(y)-abs(x)+2)
  elif x>=0 and y>=0:
    print(y-x)
  else:
    print(abs(y)-abs(x)+1)
elif abs(x)>abs(y):
  if x<0 and y<=0:
    print(abs(x)-abs(y))
  elif x>=0 and y>0:
    print(x-y+2)
  else:
    print(abs(x)-abs(y)+1)
else:
  if np.sign(x)==np.sign(y):
    print(0)
  else:
    print(1)
x,y = map(int,input().split())
if abs(x) == abs(y):
  print(1)
  exit()
if x*y > 0:
  if x < y:
    print(y-x)
  else:
    print(x-y+2)
elif x*y < 0:
  print(abs(abs(x)-abs(y))+1)
else:
  if x < y:
    print(y-x)
  else:
    print(abs(x+y)+1)
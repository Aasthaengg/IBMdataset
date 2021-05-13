x,y = map(int,input().split())
 
if abs(y) > abs(x):
  if x >= 0 and y >= 0:
    print(y-x)
  elif x < 0 and y <0:
    print(abs(y)-abs(x)+2)
  else:
    print(abs(y)-abs(x)+1)
elif abs(y) < abs(x):
  if x > 0 and y > 0:
    print(x - y + 2)
  elif x <= 0 and y <=0:
    print(abs(abs(y)-abs(x)))
  else:
    print(abs(abs(y)-abs(x))+1)
else:
  if x == y:
    print("0")
  else:
    print("1")
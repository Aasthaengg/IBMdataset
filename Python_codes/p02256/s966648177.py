x,y = map(int,input().split())

while True:
    if x >= y:
      x = x % y 
    else:
      y = y % x
    if x % y == 0:
      print(y)
      break
    elif y % x == 0:
      print(x)
      break
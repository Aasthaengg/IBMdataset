for i in range(3000):
  a = input().split()
  x = int(a[0])
  y = int(a[1])
  if x + y == 0:
    break
  elif x < y:
    print(x,y)
  elif y < x:
    print(y,x)
  else:
    print(x,y)
    


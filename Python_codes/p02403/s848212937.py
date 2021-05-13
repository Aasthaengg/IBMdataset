for i in range(10000):
  x = input().split()
  h = int(x[0])
  w = int(x[1])
  if h ==0 and w == 0:
    break
  for i in range(h):
    for i in range(w):
      print("#",end="")
    print() 
  print()

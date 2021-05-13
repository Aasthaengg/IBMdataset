import math
import sys
x=int(input())
if x==2:
  print(x)
else:
  while True:
    r=int(math.sqrt(x))
    if all(x%i!=0 for i in range(2,r)):
      print(x)
      sys.exit()
    else:
      x+=1
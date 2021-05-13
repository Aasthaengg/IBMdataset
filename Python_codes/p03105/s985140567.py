import math

a,b,c=map(int,input().split())

if a*c<=b:
  print(c)
else:
  print(math.floor(b/a))
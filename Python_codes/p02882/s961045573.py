import math
a,b,x = map(int, input().split())
x = x/a
if a*b>x*2:
  print(90-math.degrees(math.atan(2*x/b**2)))
if a*b<x*2:
  d = a*b-x
  print(math.degrees(math.atan(2*d/a**2)))
if a*b == x*2:
  print(45)
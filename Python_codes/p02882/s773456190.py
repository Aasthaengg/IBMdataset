a,b,x=map(float,input().split())
import math
if x<=a*a*b/2:
  print(math.degrees(math.atan(a*b*b/2/x)))
elif (-x/a+a*b)==0:
  print(0)
else:
  print(math.degrees(math.atan(2/a/a*(a*b-x/a))))
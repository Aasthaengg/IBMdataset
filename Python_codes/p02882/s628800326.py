a, b, x=map(int, input().split())
if a*a*b==x:
  print(0)
  exit()
import math
if 2*x/(a*b)>=a:
  ans=a/(2*b-2*x/(a**2))
else:
  ans=2*x/(a*b**2)
print(90-math.degrees(math.atan(ans)))
a,b,x=list(map(int,input().split()))
import math
import sys
if a*a*b==x:
  print(0.0000000000)
  sys.exit()

if a*a*b/2<=x:
  kakudo=a*a*a/2/(a*a*b-x)
  print(90-math.degrees(math.atan(kakudo)))
else:
  kakudo=2*x/(a*b*b)
  print(90-math.degrees(math.atan(kakudo)))


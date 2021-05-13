import math
a,b,x = map(int,input().split())

t = False
volume = a*a*b
if x <= volume/2:
  t = True
  
if t:
  tan = a*(b**2)/(2*x)
else:
  tan = 2*((a**2)*b - x)/a**3
    
print(math.degrees(math.atan(tan)))

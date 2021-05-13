import math

a,b,x = map(int,input().split())

tr = a*a*b/2

if x <= tr:
  rlt = (180/math.pi)*math.atan2(a*b**2, 2*x)
else:
  rlt = (180/math.pi)*math.atan2(2*(a**2*b - x), a**3)
  
print(rlt)
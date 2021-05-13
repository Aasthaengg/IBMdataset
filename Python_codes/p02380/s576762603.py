import math
a,b,C = input().split( )
a1 = float(a)
b1 = float(b)
C1 = float(C)
print(a1*b1*math.sin(math.radians(C1))/2)
c1 = math.sqrt(a1**2+b1**2-2*a1*b1*math.cos(math.radians(C1)))
print(a1+b1+c1)
print(b1*math.sin(math.radians(C1)))

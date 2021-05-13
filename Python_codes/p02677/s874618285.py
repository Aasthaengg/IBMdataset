import math
a,b,h,m=map(int,input().split())
h=h%12
m=m%60
deg_a=2*math.pi*(h/12+m/720)
deg_b=2*math.pi*m/60
distance=a**2+b**2-2*a*b*math.cos(deg_a-deg_b)
print(math.sqrt(distance))
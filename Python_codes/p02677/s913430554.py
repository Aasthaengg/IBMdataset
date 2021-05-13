import math
a,b,h,m= map(int, input().split())

hr = 30*h+0.5*m
mr = 6*m
ans = a**2+b**2-2*a*b*math.cos(math.radians(hr-mr))
print(math.sqrt(ans))


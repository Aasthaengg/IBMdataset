import math
a,b,h,m = map(int, input().split())

x = abs(math.pi*(h+m/60)/6 - math.pi*m/30)

ans = (a**2 + b**2 -2*a*b*math.cos(x))**0.5

print(ans)
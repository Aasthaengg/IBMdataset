import math

a,b,h,m = map(int,input().split())

ang1 = (h%12+m/60) * 30
ang2 = m * 6
ang = abs(ang1-ang2)
if ang > 180:
    ang = 360 - ang

print(math.sqrt(a**2+b**2-2*a*b*math.cos(math.radians(ang))))

a,b,C = map(float,input().split())
import math
C=math.radians(C)
S=(1/2)*a*b*math.sin(C)
c=math.sqrt(a**2+b**2-2*a*b*math.cos(C))
L=a+b+c
h=2*S/a

print(f'{S:.08f}')
print(f'{L:.08f}')
print(f'{h:.08f}')

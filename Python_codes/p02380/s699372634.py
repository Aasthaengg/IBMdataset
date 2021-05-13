import math
a,b,C = map(int,input().split())
C=math.radians(C)
S=(a*b*math.sin(C))/2
L=a+b+math.sqrt(a**2+b**2-2*a*b*math.cos(C))
h=b*math.sin(C)
print(f"{S:.8f}")
print(f"{L:.8f}")
print(F"{h:.8f}")

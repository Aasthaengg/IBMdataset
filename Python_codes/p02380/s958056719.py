import math
a,b,C=map(int,input().split())
C_rad=math.pi*C/180
S=(1/2)*a*b*math.sin(C_rad)
L=a+b+math.sqrt(a**2+b**2-2*a*b*math.cos(C_rad))
h=2*S/a
print("{0:.8f}".format(S))
print("{0:.8f}".format(L))
print("{0:.8f}".format(h))
a,b,C=map(float,input().split())
import math
d=float(math.sin(C/180*math.pi))
c=float(math.sqrt(a**2+b**2-2*a*b*math.cos((C/180)*math.pi)))
h=float('{:.6f}'.format(b*d))
L=float('{:.6f}'.format(a+b+c))
S=float('{:.6f}'.format(a*h*0.5))

print(S,L,h)

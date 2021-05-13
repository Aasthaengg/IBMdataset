import math
a,b,C=map(float,input().split())
C=math.radians(C)
c=math.sqrt(a*a+b*b-2.0*a*b*math.cos(C))
S=a*b*math.sin(C)/2.0
L=a+b+c
h=b*math.sin(C)
print("{:.8f} {:.8f} {:.8f}".format(S,L,h))


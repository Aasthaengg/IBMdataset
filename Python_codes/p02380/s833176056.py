import math
a,b,C=map(float,input().split())
s=((a*b)*math.sin(math.radians(C)))/2
S='{:.8f}'.format(s)
d=math.sqrt(a**2+b**2-2*a*b*math.cos(math.radians(C)))
L='{:.8f}'.format(a+b+d)
e=2*s/a
h='{:.8f}'.format(e)

print(S)
print(L)
print(h)

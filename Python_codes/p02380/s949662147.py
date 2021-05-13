import math
l=input().split()
a=float(l[0])
b=float(l[1])
c=int(l[2])

S=a*b*math.sin(math.radians(c))/2
h=S*2/a
d=math.sqrt(a*a+b*b-2*a*b*math.cos(math.radians(c)))
L=a+b+d

print(S)
print(L)
print(h)


import math
n=list(map(int,input().split()))

a=n[0]
b=n[1]
c=n[2]*(math.pi/180)

print(0.5*a*b*math.sin(c))
print(a+b+math.sqrt(a**2+b**2-2*a*b*math.cos(c)))
print(b*math.sin(c))


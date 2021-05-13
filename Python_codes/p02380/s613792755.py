
import math
a,b,c=(int(x) for x in input().split())

c=math.radians(c)
s=0.5*a*b*(math.sin(c))

l=a+b+(math.sqrt(a*a+b*b-2*a*b*math.cos(c)))

h=b*(math.sin(c))

print('{:.08f}'.format(s))
print('{:.08f}'.format(l))
print('{:.08f}'.format(h))

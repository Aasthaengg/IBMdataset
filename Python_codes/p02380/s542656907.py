import math

a,b,deg_c = map(float,input().split())

h = b*math.sin(math.radians(deg_c))
S = (a*h)/2
c = math.sqrt((a**2 + b**2 +(-2*a*b*math.cos(math.radians(deg_c)))))
L = a+b+c

print("{}\n{}\n{}".format(S,L,h))

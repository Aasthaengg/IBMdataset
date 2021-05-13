import math
a,b,c,d = map(float, input().split(' '))
t = (a - c)**2
h = (b - d)**2
z = t + h
print(math.sqrt(z))

import math
a, b, C = map(float, input().split())
print('{0:.8f}'.format(0.5*a*b*math.sin(math.radians(C))))
print('{0:.8f}'.format(a+b+math.sqrt(a**2+b**2-2*a*b*math.cos(math.radians(C)))))
print('{0:.8f}'.format(b*math.sin(math.radians(C))))
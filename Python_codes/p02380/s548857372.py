import math

a, b, C = map(float, raw_input().split())
print a * b * math.sin(math.radians(C)) / 2
print a + b + math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(C)))
print (b * math.sin(math.radians(C)))
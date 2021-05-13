import math
a, b, C = map(float, input().split())
print('%f' %(a * b * math.sin(math.pi * C / 180.0) / 2))
print('%f' %(a + b + math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.pi * C / 180.0))))
print(('%f' %(b * math.sin(math.pi * C / 180.0) )))
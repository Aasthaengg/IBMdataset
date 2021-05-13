import math
def hoge(a):
    return a*a
    
a, b, angle = map(float, input().split())
angle = math.radians(angle)
print (a*b*math.sin(angle) / 2)
print (a+b+math.sqrt(hoge(a) + hoge(b) - 2*a*b*math.cos(angle)))
print(a*b*math.sin(angle)/a)

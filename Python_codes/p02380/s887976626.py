import math
a,b,C=map(int,input().split())
print(f'{a*b*math.sin(math.radians(C))*1/2:.5f}')
print(f'{a+b+math.sqrt(a**2+b**2-2*a*b*math.cos(math.radians(C))):.5f}')                
print(f'{b*math.sin(math.radians(C)):.5f}')

import math

a,b,C= map(float,(input().split()))
Crad=C/180*math.pi

H = b*math.sin(Crad)
S = H * a/2


L=math.sqrt((a-b*math.cos(Crad))**2+H**2)+a+b
print(S)
print(L)
print(H)
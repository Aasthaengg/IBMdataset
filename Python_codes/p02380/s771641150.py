import math
a,b,C = map(int, input().split())
c = C/180 * math.pi
S = (1/2)*a*b*math.sin(c)
x = math.sqrt(a**2+b**2-2*a*b*math.cos(c))
print(S)       #面積1/2*absinC
print(a+b+x)  #辺の長さa^2=b^2+c^2-2bccosA→周の長さa+b+c
print(2*S/a)     #高さh 面積S=1/2*a*h→h=2*S/a

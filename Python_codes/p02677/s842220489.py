import math
A,B,H,M = map(int,input().split())
tyousindeg = M*360/60
tannsinndeg = H*360/12+30*M/60
lst = sorted([tyousindeg,tannsinndeg])
C = lst[1]-lst[0]
if C > 180:
  C = 360 - C
kyori = math.sqrt(A**2+B**2-2*A*B*math.cos(math.radians(C)))
print(kyori)
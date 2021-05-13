import math

a,b,H,M = list(map(int,input().split()))

angle=abs((H*30+M/2)-M*6)/360*2*math.pi
print((a**2+b**2-2*a*b*math.cos(angle))**0.5)

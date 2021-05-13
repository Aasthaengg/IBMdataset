import math
a,b,h,m=map(int,input().split())

p=abs(((h*360)/12)+((m*30)/60)-m*6)
q=math.radians(p)
c=a**2+b**2-2*a*b*math.cos(q)
print(math.sqrt(c))

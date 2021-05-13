import math
a,b,c=map(float,input().split())
print((a*b)*math.sin(math.radians(c))/2)
print(a+b+math.sqrt(pow(a,2)+pow(b,2)-2*a*b*math.cos(math.radians(c))))
print((a*b)*math.sin(math.radians(c))/a)
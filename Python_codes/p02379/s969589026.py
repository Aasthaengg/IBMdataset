import math
a,b,c,d=map(float,input().split())

x=abs(c-a)
y=x**2

z=abs(d-b)
w=z**2
t=math.sqrt(y+w)

print(f'{t:.8f}')

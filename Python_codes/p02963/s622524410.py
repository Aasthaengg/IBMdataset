import math

s=int(input())

n=math.ceil(math.sqrt(s))

if n*n-s<0:
  n+=1

x2=n
y3=n

while x2*y3-s>10**9:
  y3-=1

y2=x2*y3-s
x3=1

print(0,0,x2,y2,x3,y3)
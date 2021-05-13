import math

x=int(input())
a=int(input())
b=int(input())

x=x-a
c=math.floor(x/b)
print(x-c*b)
import math
a,b,x=map(int,input().split())
v = a * b
x = x / a
if x < v/2:
    c = x * 2 / b
    print(math.degrees(math.atan(b/c)))
else:
    rest = v - x
    c = rest * 2 / a
    print(math.degrees(math.atan(c/a)))
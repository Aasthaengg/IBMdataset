import math
S = int(input())
x1 = 10**9
y2 = math.ceil(S/x1)
x2 = 1
y1 = x1*y2 - S
x3,y3 = 0,0
print(x1,y1,x2,y2,x3,y3)
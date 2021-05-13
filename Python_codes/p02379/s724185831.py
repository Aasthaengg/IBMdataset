import math

x1 , y1 , x2 , y2 = map(float,input().split())

a = abs(x1-x2)
b = abs(y1-y2)

ans = math.sqrt(a**2 + b**2)

print('{:.9f}'.format(ans))

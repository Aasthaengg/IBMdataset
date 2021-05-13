import math  #include<math.h>

x1,y1,x2,y2 = map(float, input().split())
x = abs(x1 - x2)
y = abs(y1 - y2)

print(math.sqrt(x*x + y*y))



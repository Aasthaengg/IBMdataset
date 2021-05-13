import math

x1,x2,x3,x4 = map(float, input().split())
n = (x3 - x1)**2 + (x4 - x2)**2
ans = math.sqrt(n)
print(ans)

import math
n, d = map(int,input().split())
ans = 0
for i in range(n):
  x, y = map(int,input().split())
  z = math.sqrt(x**2 + y**2)
  if (z <= d):
    ans = ans + 1
print(ans)
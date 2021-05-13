import math
n,d = list(map(int, input().split()))
c=0
for i in range(n):
  x,y = list(map(int, input().split()))
  if x*x + y*y <= d*d:
    c += 1
  a=math.sqrt(10)
print(c)
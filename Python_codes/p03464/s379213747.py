import math
n = int(input())
a = [int(i) for i in input().split()]
mi = 2
ma = 2
for b in a[::-1]:
  mi = math.ceil(mi/b)*b
  ma = math.ceil((ma+1)/b)*b-1
  if ma < b or mi > ma:
    print(-1)
    exit()
print(mi,ma)
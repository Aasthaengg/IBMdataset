a = input().split()
b = int(a[0])
c = int(a[1])
import math

minb = math.ceil(b * 12.5)

if b % 2 == 1:
  maxb = int((b+1) * 12.5 - 1)
else:
  maxb = int(math.floor((b+1) * 12.5))

minc = c * 10
maxc = (c+1) * 10 - 1

if max([minb,minc]) <= min([maxb,maxc]):
  print(max([minb,minc]))
else:
  print("-1")
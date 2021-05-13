import math
n=int(input())
a=[int(input()) for i in range(5)]
b=0
for i in range(5):
  b=max(math.ceil(n/a[i]),b)
print(5+b-1)
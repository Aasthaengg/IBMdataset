import math
n=int(input())
a=[0]*5
for i in range(5):
  a[i]=math.ceil(n/int(input()))
print(max(a)+4)
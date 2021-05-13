import math
from decimal import Decimal
n,k=map(int,input().split())
a=[0]*(n+1)
for x in range(1,n+1):
  a[x] = max(0, math.ceil(math.log(k,2)- math.log(x,2)))
bunsi = 0
for x in range(1,n+1):
  bunsi += 2**(a[1]-a[x])
print(Decimal(bunsi/(n*2**a[1])))
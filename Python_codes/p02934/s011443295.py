n = int(input())
a = list(map(int,input().split()))
from decimal import Decimal as dec
s = 0
for i in range(n):
    s += dec(1 / a[i])
print(dec(1 / s))
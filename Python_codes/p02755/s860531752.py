import math
import sys

A, B = list(map(int, input().split()))
for i in range(1001):
  priceA = math.floor(i*1.08)
  priceB = math.floor(i*1.10)
  taxA = priceA - i 
  taxB = priceB - i 
  if taxA == A and taxB == B:
    print(i)
    sys.exit()
print("-1")  
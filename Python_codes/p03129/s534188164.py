
import math

n,k = map(int,input().strip().split())

if math.ceil(n/2) >= k:
  print("YES")
else:
  print("NO")
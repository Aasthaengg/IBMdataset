import math
A, B, C =map(int, input().split())
if B >= A * C:
  print(C)
else:
  print(math.floor(B/A))

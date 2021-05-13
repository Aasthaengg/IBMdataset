import math
A, B, C = map(int, input().split())
if C % math.gcd(A, B):
  print('NO')
else:
  print('YES')
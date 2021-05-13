import math
a, b = input().split()
ab = int(a + b)
result = math.sqrt(ab)
value = result % 1
if result * result == ab and value == 0:
  print('Yes')
else:
  print('No')
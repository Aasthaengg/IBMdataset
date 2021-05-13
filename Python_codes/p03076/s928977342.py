a = [ int(input()) for _ in range(5) ]
import math
#a = [123,123,123,123,123]
b = 0
total = 0
for i in a:
  x = math.ceil(i / 10) * 10
  b = max(b, x - i)
  total += x

print(total - b)

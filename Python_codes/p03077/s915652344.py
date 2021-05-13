import math
n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

m = [a, b, c, d, e]
max_t = -1
for i in range(5):
  t = math.ceil(n / m[i])
  max_t = max(max_t, t)

print(max_t+4)
import math
res = float('inf')
L, R = map(int, input().split())
length = min(R - L, 3000)
for i in range(L, L + length):
  for j in range(i+1, L + length + 1):
    temp = (i * j) % 2019
    if temp < res:
      res = temp
print(res)
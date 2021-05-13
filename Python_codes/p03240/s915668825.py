# solution

import math
import io

data = int(input())

array = [list(map(int, input().split())) for _ in range(data)]

n, m, k = list(filter(lambda n: n[2], array))[0]

for i in range(101):
  for j in range(101):
    kite = k + abs(n-i) + abs(m-j)
    if all(max(kite-abs(t[0]-i)-abs(t[1]-j), 0) == t[2] for t in array):
      print(i,j,kite)
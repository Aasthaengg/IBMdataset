# AtCoder Petrozavodsk Contest 001 - A
# -*- encoding: UTF-8 -*-
x, y = map(int, input().split())

result = -1

if x % y == 0 :
  result = -1
else: 

  n = (10 ** 18) // x

  for i in range(2, n+1) :
    m = x * i
    if (m % y) != 0 :
      result = m
      break

print(result)

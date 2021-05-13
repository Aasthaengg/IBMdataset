# -*= coding: utf-8 -*-

A, B = map(int, input().split())
x = 25 * A // 2

for x in range(B * 10 + 0, B * 10 + 10, 1):
  if round(x * 8 // 100) == A:
    print(x)
    exit()
print('-1')
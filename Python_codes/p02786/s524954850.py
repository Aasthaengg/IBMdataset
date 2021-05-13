# -*- coding: utf-8 -*-
H = int(input())
h = H
count = 1
total_count = count
while h > 1:
  count *= 2
  total_count += count
  h //= 2
print(total_count)
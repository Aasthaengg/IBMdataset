# -*- coding: utf-8 -*-
import numpy
n, d = map(int, input().split())

li = []
for i in range(n):
  x, y = map(int,input().split())
  li.append([x, y])

answer = 0
for i in li:
  if numpy.sqrt(i[0]**2 + i[1]**2) <= d:
    answer += 1
print(answer)
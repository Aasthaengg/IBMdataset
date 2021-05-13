# -*- coding: utf-8 -*-
# 整数の入力
nab = [int(s) for s in input().split()]

N = nab[0]
A = nab[1]
B = nab[2]

count = 0
for i in range(N):
  target = str(i+1)
  total = 0
  for j in range(len(target)):
    total = total + int(target[j])

  if total >= A and total <= B:
    count = count + int(target)

print(count)

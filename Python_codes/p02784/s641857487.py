# -*- coding: utf-8 -*-
H, N = map(int, input().split())
A = list(map(int, input().split()))

total = 0
for i in range(N):
  total += A[i]
if total >= H:
  print("Yes")
else:
  print("No")
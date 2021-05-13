# -*- coding: utf-8 -*-
N, M = map(int, input().split())
metro = {i:0 for i in range(N)}

for _ in range(M):
  a, b = map(int, input().split())
  metro[a-1] += 1
  metro[b-1] += 1

for i in range(N):
  print(metro[i])
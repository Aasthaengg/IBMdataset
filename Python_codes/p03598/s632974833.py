# -*- coding: utf-8 -*-
N = int(input())
K = int(input())
balls = list(map(int, input().split()))
mv = 0
border = (K-1) // 2
for ball in balls:
  if ball <= border:
    mv += ball * 2
  else:
    mv += abs((K - ball) * 2)
print(mv)


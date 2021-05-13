# -*- coding: utf-8 -*-
N = int(input())
K = int(input())
X = int(input())
Y = int(input())
cost = 0
if N <= K:
  cost = N * X
else:
  cost = ((N-K) * Y) + (K * X)
print(cost)
# -*- coding: utf-8 -*-
import sys
import numpy as np

N,S, *A = map(int, sys.stdin.buffer.read().split())
mod = 998244353
A = sorted(A)

answer = np.zeros(3002).astype(np.int64)
power2 = 1

total = 0
for a in A:
  total = min(3001,a+total)
  answer[a+1:total+1] = (2*answer[a+1:total+1]+answer[1:total-a+1])%mod
  answer[a] = (2*answer[a]+power2)%mod
  answer[1:a] = (2*answer[1:a])%mod
  power2 = (2*power2)%mod

print(answer[S])
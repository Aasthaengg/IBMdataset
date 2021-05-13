# -*- coding: utf-8 -*-
N, K = map(int, input().split())
p = list(map(int, input().split()))

total = [0] * N
total[0] = p[0]
for i in range(1, N):
  total[i] = total[i-1] + p[i]

total_K = 0
max_i = 0
for i in range(N-K+1):
  if i == 0:
    total_K = total[K-1]
  else:
    if total[i+K-1] - total[i-1] > total_K:
      total_K = total[i+K-1] - total[i-1]
      max_i = i

ans = 0
for i in range(K):
  ans += (p[max_i + i] + 1) / 2
print(ans)
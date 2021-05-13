# -*- coding: utf-8 -*-
N, K = map(int, input().split())
A = list(map(int, input().split()))
A.insert(0, None)

history = [None] * (N+1)

next_town = 1
i = 0
skip_flg = False
while i < K:
  if history[next_town] == None:
    history[next_town] = i
  elif skip_flg == False:
    skip_flg = True
    
    i = i + ((K - i)//(i - history[next_town])) * (i - history[next_town])
  if i < K:
    i += 1
    next_town = A[next_town]
print(next_town)
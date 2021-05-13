import numpy as np
n = int(input())
s = [int(input()) for _ in range(n)]

if np.all(np.array(s) % 10 == 0):
  print(0)
  exit()

s.sort()
score = sum(s)
i = -1
while score % 10 == 0:
  i += 1
  if s[i] % 10 == 0:
    continue
  score -= s[i]
  if i == n:
    break
  
print(score)
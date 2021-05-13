from bisect import bisect
import math

N, H = map(int, input().split())
A = []
B = []

for _ in range(N):
  a, b = map(int, input().split())
  A.append(a)
  B.append(b)

aM = max(A)
B.sort()

r = N - bisect(B, aM)
cnt = 0

for i in range(r):
  H -= B[-1-i]
  cnt += 1
  if H <= 0:
    print(cnt)
    break
  
if H > 0:
  print(math.ceil(H/aM) + cnt)
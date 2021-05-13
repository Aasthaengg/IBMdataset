import numpy as np
N, M = [int(x) for x in input().split()]
H = [float(x) for x in input().split()]
AB = [[int(x) for x in input().split()] for _ in range(M)]

max_h = [0 for _ in range(N)]

for A, B in AB:
  max_h[A-1] = max(max_h[A-1], H[B-1])
  max_h[B-1] = max(max_h[B-1], H[A-1])

ans = 0
for i in range(N):
  if(H[i]>max_h[i]):
    ans += 1
print(ans)
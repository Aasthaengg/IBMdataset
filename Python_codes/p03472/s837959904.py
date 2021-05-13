
import math

N,H = map(int, input().split())
A = 0
B = []
for i in range(N):
  a,b = map(int, input().split())
  A = max(A, a)
  B.append(b)

B.sort(reverse=True)

accum_B = [0] * (N+1)
for i in range(1, N+1):
  accum_B[i] = accum_B[i-1] + B[i-1]

ans = H+1
for i in range(N+1):
  if H - accum_B[i] <= 0:
    ans = min(ans, i)
  else:
    ans = min(ans, i + math.ceil((H - accum_B[i]) / A))

print(ans)

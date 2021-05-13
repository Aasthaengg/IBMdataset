N, M = map(int, input().split())
mod = 10 ** 9 + 7
A = [1] * (N+1)
for i in range(M):
  A[int(input())] = 0
if N == 1:
  print(1)
else:
  p = 1
  q = 1
  for i in range(2, N+1):
    r = A[i-2] * p + A[i-1] * q
    p = q
    q = r % mod
  print(q)
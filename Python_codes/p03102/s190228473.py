N, M, C = map(int, input().split())
B = list(map(int, input().split()))
res = 0
A = []
for i in range(N):
  A = list(map(int, input().split()))
  tot = C
  for j in range(M):
    tot += A[j] * B[j]
  if tot > 0:
    res += 1
print(res)


N, M, C = (int(x) for x in input().split())
B = [int(x) for x in input().split()]
ans = 0
for i in range(N):
  A = [int(x) for x in input().split()]
  P = C
  for j in range(M):
    P += A[j]*B[j]
  if P > 0:
    ans += 1
print(ans)
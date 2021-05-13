N, M, C = map(int, input().split())
B = list(map(int, input().split()))
ans = 0
for i in range(N):
  a = list(map(int, input().split()))
  p = C
  for j in range(M):
    p += a[j] * B[j]
  if p > 0:
    ans += 1
print(ans)
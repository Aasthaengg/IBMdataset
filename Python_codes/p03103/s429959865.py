N, M= map(int, input().split())
A = []
for i in range(N):
  A.append(list(map(int, input().split())))
A.sort()
ans = 0
for i in range(N):
  if A[i][1] < M:
    ans += A[i][0] * A[i][1]
    M -= A[i][1]
  else:
    ans += A[i][0] * M
    break
print(ans)
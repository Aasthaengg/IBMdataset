N, x = map(int, input().split())
A = sorted(list(map(int, input().split())))

cnt = 0
for i in range(N):
  if i == N - 1:
    if x == A[i]:
      cnt += 1
      x -= A[i]
  else:
    if x >= A[i]:
      cnt += 1
      x -= A[i]

print(cnt)

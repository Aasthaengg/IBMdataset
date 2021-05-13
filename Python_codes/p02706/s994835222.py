N, M = map(int, input().split())
A = list(map(int, input().split()))
count = 0

for i in range(M):
  count += A[i]

if(count <= N):
  print(N - count)
else:
  print(-1)
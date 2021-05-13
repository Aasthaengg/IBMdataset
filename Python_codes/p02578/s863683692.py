N = int(input())
A = list(map(int, input().split()))
ans = 0
M = -1

for i in range(N):
  M = max([M, A[i]])
  if A[i] < M:
    ans += M - A[i]
print(ans)

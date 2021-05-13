N, M = map(int, input().split())
id = [0] * N
ans = 0
for _ in range(M):
  L, R = map(int, input().split())
  id[L-1] += 1
  if R != N:
    id[R] -= 1
for i in range(N):
  if i != 0:
    id[i] += id[i-1]
  if id[i] == M:
    ans += 1
print(ans)
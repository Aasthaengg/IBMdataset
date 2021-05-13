import math

N, D = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
  dist = L[i][0] ** 2 + L[i][1] ** 2
  if math.sqrt(dist) <= D:
    ans += 1

print(ans)
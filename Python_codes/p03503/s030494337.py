N = int(input())
F = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]

ans = -10000000000
for bit in range(1, 1<<10):
  now = 0
  for i in range(N):
    c = 0
    for j in range(10):
      if (1&bit>>j) & F[i][j]:
        c += 1
    now += P[i][c]
  ans = max(ans, now)
print(ans)
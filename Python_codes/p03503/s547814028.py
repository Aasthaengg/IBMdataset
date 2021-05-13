N = int(input())
F = [list(map(int, input().split())) for i in range(N)]
P = [list(map(int, input().split())) for i in range(N)]

ans = -float('inf')

for i in range(1, 2**10):
  c = [0] * N
  for j in range(10):
    if i>>j & 1:
      for k in range(N):
        c[k] += F[k][j]
  profit = sum([P[k][c[k]] for k in range(N)])
  ans = max(ans, profit)

print(ans)
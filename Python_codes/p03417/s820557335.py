N, M = map(int, input().split())
N, M = min(N,M), max(N,M)

ans = [[1], [2, 0], [3, 0, 9], [2, 0, 6, 4]]
if M <= 4:
  print(ans[M-1][N-1])
  exit()
if N == 1:
  print(M-2)
  exit()
if N == 2:
  print(0)
  exit()
if N == 3:
  print(N*M - 6)
  exit()

print(4 + (N-4 + M-4)*2 + (N-4)*(M-4))
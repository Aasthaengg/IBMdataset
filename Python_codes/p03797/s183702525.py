
N, M = map(int, input().split())

if N * 2 >= M:
  print(M//2)
else:
  diff = M//2 - N
  print(N+diff//2)
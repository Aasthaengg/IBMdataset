N, K = map(int, input().split())

if K == 1:
  print(0)
  exit()

if N > K:
  print(N - K)
else:
  print(0)
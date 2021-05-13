N, M = map(int, input().split())
N, M = min(N, M), max(N, M)

if N != 1 and M != 1:
  print((N-2)*(M-2))
elif N == 1 and M != 1:
  print(M-2)
else:
  print(1)
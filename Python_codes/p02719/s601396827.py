N, K = list(map(int, input().split()))

N = N % K

if N < K - N:
  print(N)
else:
  print(K - N)
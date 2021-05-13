N, M = map(int, input().split())

if M < 2*N:
  print(M//2)
else:
  base = N
  M -= 2*N
  print(base + M//4)
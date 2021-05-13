N, M = map(int, input().split())

if N == 2 or M == 2:
  print(0)
elif N == 1:
  print(abs(M-2))
elif M == 1:
  print(abs(N-2))
else:
  print((N-2) * (M-2))
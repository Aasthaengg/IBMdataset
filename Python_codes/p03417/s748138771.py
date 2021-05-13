N, M = map(int, input().split())

if N >= 3 and M >= 3:
  print(N*M - (2*N + 2*M - 4))
elif N == 2 or M == 2:
  print(0)
elif N == 1 and M == 1:
  print(1)
elif N == 1:
  print(M - 2)
elif M == 1:
  print(N - 2)
else:
  print(1)

import sys

N, M, K = map(int, input().split())

for n in range(0, N+1):
  for m in range(0, M+1):
    if (N - n) * m + n * (M - m) == K:
      print("Yes")
      sys.exit()
print("No")
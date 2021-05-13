import sys
readline = sys.stdin.readline

N,M,K = map(int,readline().split())

for a in range(N + 1):
  for b in range(M + 1):
    if a * (M - b) + (N - a) * b == K:
      print("Yes")
      exit(0)
else:
  print("No")
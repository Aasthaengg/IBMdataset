import sys

N, M = map(int, input().split())

if N == 1 and M == 1:
  print(1)
  sys.exit()

if N == 1:
  print(M - 2)
  sys.exit()
  
if M == 1:
  print(N - 2)
  sys.exit()

print(N * M - (N * 2 + M * 2 - 4))
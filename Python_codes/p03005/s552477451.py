import sys
N, K = map(int, sys.stdin.readline().split())

if K == 1:
  print(0)
else:
  print(N-K)
from sys import stdin
N, K = [int(_) for _ in stdin.readline().rstrip().split()]
if K == 1:
  print(0)
else:
  print(N-K)
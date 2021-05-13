import numpy
N, K, Q = map(int, input().split())
A = [int(input()) for i in range(Q)]
p = numpy.full(N, K)
for i in A:
  p -= 1
  p[i-1] += 1
for i in range(N):
  print('Yes' if p[i] > 0 else 'No')
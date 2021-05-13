import collections
N,M = map(int, input().split())

A = [list(map(int, input().split())) for i in range(M)]

c = collections.Counter(sum(A,[]))

for i in range(1, N+1):
  print(c[i])
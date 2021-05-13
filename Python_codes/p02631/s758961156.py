N, *D = map(int, open(0).read().split())
ALL = 0
for d in D:
  ALL ^= d
D = map(lambda x: x ^ ALL, D)
print(*D, sep=' ')
N, M = map(int, input().split())
a = sum([list(map(int, input().split())) for _ in range(M)], [])
for n in range(1, N+1):
  print(a.count(n))
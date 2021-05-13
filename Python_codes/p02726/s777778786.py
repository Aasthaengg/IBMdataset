N, X, Y = map(int, input().split())
d = [0 for i in range(N)]
for a in range(1, N):
  for b in range(a+1, N+1):
    dest = min(b-a, abs(b-Y)+abs(a-X)+1)
    d[dest] += 1
for n in d[1:]:
  print(n)
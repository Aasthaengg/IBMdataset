N, X = map(int, input().split())
d = 1001

for _ in range(N):
  m = int(input())
  X -= m
  d = min(d, m)

print(N + X//d)
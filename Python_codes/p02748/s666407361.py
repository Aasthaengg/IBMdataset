A, B, M = map(int, input().split())
a = [int(e) for e in input().split()]
b = [int(e) for e in input().split()]

ans = min(a) + min(b)

for _ in range(M):
  x, y, c = map(int, input().split())
  cost = a[x - 1] + b[y - 1] - c
  ans = min(ans, cost)

print(ans)

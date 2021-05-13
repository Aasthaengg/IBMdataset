n, a, b = map(int, input().split())
town = list(map(int, input().split()))
dist = []
for i in range(n-1):
  dist.append((town[i+1]-town[i])*a)

ans = 0
for i in range(n-1):
  ans += min(dist[i], b)
print(ans)
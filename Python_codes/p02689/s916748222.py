n,m = map(int, input().split())
h = list(map(int, input().split()))

ab = [0]*n
for _ in range(m):
  a,b = map(lambda x: int(x)-1, input().split())
  ab[a] = max(ab[a], h[b])
  ab[b] = max(ab[b], h[a])
  
ans = 0
for i in range(n):
  if ab[i] < h[i]: ans += 1
print(ans)
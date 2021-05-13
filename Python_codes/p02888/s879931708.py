import bisect
n = int(input())
edges = sorted(list(map(int, input().split(' '))))
ans = 0
for i in range(n-1, -1, -1):
  for j in range(i-1, -1, -1):
    limit = edges[i] - edges[j]
    if limit < edges[j]:
      index = bisect.bisect_right(edges, limit)
      ans += max(0, j - index)  # maxいらんかも
print(ans)

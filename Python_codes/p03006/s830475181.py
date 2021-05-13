from collections import defaultdict

N = int(input())
xy = [list(map(int, input().split())) for i in range(N)]

d = defaultdict(int)
for i, (xi, yi) in enumerate(xy):
  for j, (xj, yj) in enumerate(xy):
    p, q = xi - xj, yi - yj
    d[(p, q)] += 1

d.pop((0, 0))
ans = N
for k in d:
  ans = min(ans, N-d[k])

print(ans)
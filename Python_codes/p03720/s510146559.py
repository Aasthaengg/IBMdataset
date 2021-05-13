n, m = map(int, input().split())
cnt_roads = [0] * n
for _ in range(m):
  a, b = map(int, input().split())
  cnt_roads[a-1] += 1
  cnt_roads[b-1] += 1
for cnt in cnt_roads:
  print(cnt)

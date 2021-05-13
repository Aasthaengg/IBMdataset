n, m = map(int, input().split())
ka = [list(map(int, input().split())) for i in range(n)]
l = [True] * m
for i in ka:
  K = i[0]
  for j in range(m):
    if j+1 not in i[1:]:
      l[j] = False
print(l.count(True))
def warshal_floyd(d):
  for k in range(n):
    for i in range(n):
      for j in range(n):
        d[i][j] = min(d[i][j], d[i][k]+d[k][j])
  return d

n, m = map(int, input().split())
INF = 10**18
d = [[INF for i in range(n)] for j in range(n)]
e = [[0, 0, 0] for _ in range(m)]
for i in range(m):
    a, b, c = map(int, input().split())
    a, b = a-1, b-1
    d[a][b] = c
    d[b][a] = c

    e[i][0] = a
    e[i][1] = b
    e[i][2] = c

for i in range(n):
    d[i][i] = 0

d = warshal_floyd(d)
ans = 0
for i in range(m):
    a = e[i][0]
    b = e[i][1]
    c = e[i][2]
    for k in range(n):
        if d[a][k] == c + d[b][k]:
            break
    else:
        ans += 1
print(ans)
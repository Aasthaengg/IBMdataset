import sys
input = sys.stdin.readline
N, M = map(int, input().split())

s = [tuple(map(int, input().split())) for _ in range(N)]
s.sort(key = lambda x: -x[1])
table = [(-1, -1)] * (N + 1)
c = 0
for i in range(N):
  if table[s[i][0]] == (-1, -1):
    table[s[i][0]] = (i, s[i][1])
    c += 1

table.sort(key = lambda x: -x[1])
res = [0] * (min(c, M) + 1)
vis = set()
p = M
for i in range(M): res[0] += s[i][1]
for x in range(1, min(c, M) + 1):
  res[x] = res[x - 1] + pow(x, 2) - pow(x - 1, 2)
  if table[x - 1][0] >= M:
    res[x] += table[x - 1][1]
    p -= 1
    while p in vis:
      p -= 1
    res[x] -= s[p][1]
  vis.add(table[x - 1][0])
  #print(p)
print(max(res))

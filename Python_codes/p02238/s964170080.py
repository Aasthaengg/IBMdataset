t = 1
v, d, f = {}, {}, {}

def dfs(i):
  global t, v, d, f
  if i in d:
    return
  if i != 0:
    d[i] = t
    t += 1
  for j in v[i]:
    dfs(j)
  if i != 0:
    f[i] = t
    t += 1

n = int(input())
v[0] = list(range(1, n+1))
for i in range(n):
  tmp = list(map(int, input().split()))
  v[tmp[0]] = tmp[2:]
  v[tmp[0]].sort()
dfs(0)
for i in range(n):
  print("{} {} {}".format(i+1, d[i+1], f[i+1]))


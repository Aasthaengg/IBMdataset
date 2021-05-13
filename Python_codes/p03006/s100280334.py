import sys
input = sys.stdin.readline

N = int(input())
b = [list(map(int, input().split())) for _ in range(N)]
b.sort(key = lambda x: (x[0], x[1]))
vis = set()
viss = set()
res = 0
def dfs(n, p, q):
  global vis
  global viss
  res = 0
  vis.add(n)
  viss.add(n)
  for k in range(N):
    if k in vis: continue
    if k in viss: continue
    if (b[k][0] == b[n][0] + p) and (b[k][1] == b[n][1] + q):
      res = max(res, dfs(k, p, q))
  vis.discard(n)
  return res + 1
for i in range(N):
  for j in range(N):
    vis = set()
    viss = set()
    p = b[j][0] - b[i][0]
    q = b[j][1] - b[i][1]
    temp = 0
    for n in range(N):
      if n in viss: continue
      t = dfs(n, p, q)
      if t > 1:
        temp += t - 1
    res = max(temp, res)
    #print(temp, p, q)
print(N - res)
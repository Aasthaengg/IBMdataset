import sys
sys.setrecursionlimit(10**9)

N,M = map(int,input().split())
G = [[] for _ in [0]*N]

for _ in [0]*M:
  a, b, d = map(int, input().split())
  a -= 1
  b -= 1
  G[a].append((b, d))
  G[b].append((a, -d))

X = [None]*N

def dfs(i, x=0):
  for j, d in G[i]:
    if X[j] is None:
      X[j] = x+d
      dfs(j, x+d)
    elif X[j] != x+d:
      print('No')
      exit()

for i in range(N):
  if X[i] is not None:
    continue
  X[i] = 0
  dfs(i)
print('Yes')
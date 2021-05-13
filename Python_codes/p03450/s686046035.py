import sys
sys.setrecursionlimit(10**9)
N,M = map(int,input().split())
G = [[] for n in range(N)]

for m in range(M):
  a,b,d = map(int,input().split())
  G[a-1].append((b-1,d))
  G[b-1].append((a-1,-d))

X = [None]*N

def dfs(i, x=0):
  for j, d in G[i]:
    if X[j] is None:
      X[j] = x+d
      dfs(j, x+d)
    elif X[j] != x+d:
      print("No")
      exit()

for n in range(N):
  if X[n] is not None:
    continue
  X[n] = 0
  dfs(n)

print("Yes")
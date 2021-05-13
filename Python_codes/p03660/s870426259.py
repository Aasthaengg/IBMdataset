import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())
E = [set() for _ in range(N)]
for i in range(N-1):
  a,b = map(int,input().split())
  E[a-1].add(b-1)
  E[b-1].add(a-1)

V = [-1 for _ in range(N)]
def dfs(u,count):
  V[u] = count
  for v in E[u]:
    if V[v] == -1:
      dfs(v,count+1)
dfs(0,0)
Path = []
v = N-1
while (v != 0):
  Path.append(v)
  for u in E[v]:
    if V[u] == V[v] -1:
      v = u
Path.append(0)
#print(Path)

def dfs2(u):
  visited[u] = True
  res = 1
  for v in E[u]:
    if not visited[v]:
      res += dfs2(v)
  return res
visited = [False for _ in range(N)]
for i in Path:
  visited[i] = True
fennec = 0
for i in range((len(Path)+1)//2):
  fennec += dfs2(Path[-i-1])
snuke = 0
for i in range(len(Path)//2):
  snuke += dfs2(Path[i])
#print(fennec,snuke)
print('Fennec' if fennec > snuke else 'Snuke')

n = int(input())
g = [[] * n for i in range(n)]
for i in range(n-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)
    
da = [0]*n
dn = [0]*n
from collections import deque

def bfs(s,d):
  que = deque()
  que.append((s,1))
  chk = [False]*n
  chk[s] = True
  cnt = 1
  while que:
      now,p = que.popleft()
      if cnt == n:
        break
      for i in g[now]:
          if not chk[i]:
            d[i] = p
            chk[i] = True
            cnt += 1
            que.append((i,p+1))
            
bfs(0,da)
bfs(n-1,dn)

f = 0
s = 0
for i in range(n):
  if da[i] <= dn[i]:
    f += 1
  else:
    s += 1
if f > s:
  print('Fennec')
else:
  print('Snuke')
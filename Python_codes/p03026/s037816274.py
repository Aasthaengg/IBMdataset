n = int(input())
g = [[] * n for i in range(n)]
for i in range(n-1):
  u, v = map(int, input().split())
  u -= 1
  v -= 1
  g[u].append(v)
  g[v].append(u)
  
d = list(map(int,input().split()))
d.sort(reverse=True)

from collections import deque
 
que = deque()
que.append(0)
chk = [False]*n
chk[0] = True
ans = [0]*n
ans[0] = d[0]
cnt = 1
while que:
  now = que.popleft()
  if cnt == n:
    break
  for i in g[now]:
    if not chk[i]:
      chk[i] = True
      ans[i] = d[cnt]
      cnt += 1
      que.append(i)
      
print(sum(d[1:]) if n > 1 else 0)
print(*ans)
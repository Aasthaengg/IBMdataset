from collections import deque
from collections import Counter

H,W=map(int,input().split())
S=[]
c = []
for i in range(H):
  s = input()
  S.append(s)
  c.extend(list(s))
c = Counter(c)

def bfs(s):
  seen = [[0 for i in range(W)] for j in range(H)]
  total = [[0 for i in range(W)] for j in range(H)]
  todo = deque([])
  now = s
  if S[now[0]][now[1]]=='#':return 0
  seen[now[0]][now[1]],total[now[0]][now[1]] = 1,0
  todo.append(now)
  while 1:
    if len(todo)==0:break
    now = todo.popleft()
    for d in [(1,0),(-1,0),(0,1),(0,-1)]:
      new = (now[0]+d[0], now[1]+d[1])
      if new[0]<0 or new[0]>=H:continue
      if new[1]<0 or new[1]>=W:continue
      if seen[new[0]][new[1]]==1:continue
      if S[new[0]][new[1]]=='#':continue
      seen[new[0]][new[1]] = 1
      todo.append(new)
      total[new[0]][new[1]] = total[now[0]][now[1]] + 1
  return total

d = bfs((0,0))[-1][-1]
if d == 0:
  print(-1)
  exit()
print(c['.']-d-1)
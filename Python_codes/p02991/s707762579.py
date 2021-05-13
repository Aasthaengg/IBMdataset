N,M=map(int,input().split())
E=[[] for i in range(N)]
for i in range(M):
  u,v=map(int,input().split())
  u,v=u-1,v-1
  E[u].append(v)
S,T=map(int,input().split())
S,T=S-1,T-1

from collections import deque
q=deque()
seen=[[False for i in range(3)] for j in range(N)]
q.append([S,0,1])
while q:
  node=q.popleft()
  v=node[0]
  step=node[1]
  turn=node[2]
  if step==3:
    if v==T:
      print(turn)
      break
    step=0
    turn+=1
  if seen[v][step]:
    continue
  seen[v][step]=True
  children=E[v]
  for child in children:
    q.append([child,step+1,turn])
else:
  print(-1)

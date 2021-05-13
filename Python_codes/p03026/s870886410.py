N=int(input())
G=[[] for _ in range(N)]
for i in range(N-1):
  a,b=map(int,input().split())
  G[a-1].append(b-1)
  G[b-1].append(a-1)
  
*c,=map(int,input().split())

from collections import deque

def bfs(s):
    seen = [0]*N
    d = [0]*N
    prev = [0]*N
    todo = deque()
    seen[s]=1
    todo.append(s)
    while len(todo):
      a = todo.popleft()
      for b in G[a]:
        if seen[b] == 0:
          seen[b] = 1
          todo.append(b)
          d[b] += d[a] + 1
          prev[b] = a
    return d, prev

d, prev = bfs(0)
order = list(zip(*sorted(enumerate(d), key=lambda x:x[1])))[0]

dp = [1]*N
for v in order[::-1]:
    if len(G[v])==0:
        dp[v] = 1
    dp[prev[v]] += dp[v]
    
sizes=[0]*N
for i in range(N):
  if i == 0:
    tmp = max([dp[v] for v in G[i]])
    sizes[i]=tmp
    continue
  tmp = max(dp[i]-1,N-dp[i])
  sizes[i]=tmp
  
MIN=10**20
argmin=-1
for i in range(N):
  if sizes[i]<MIN:
    MIN=sizes[i]
    argmin=i
    
c = sorted(c,reverse=True)
score=[0]*N
score[argmin]=c[0]

def bfs2(s):
    i = 1
    seen = [0]*N
    todo = deque()
    seen[s]=1
    todo.append(s)
    while len(todo):
      a = todo.popleft()
      for b in G[a]:
        if seen[b] == 0:
          seen[b] = 1
          todo.append(b)
          score[b] = c[i]
          i += 1
    return 
  
bfs2(argmin)

ans=0
for i in range(N):
  for j in G[i]:
    if i>j:continue
    ans += min(score[i],score[j])
    
print(ans)
print(*score)
from collections import deque

N=int(input())
G=[[] for _ in range(N+1)]

for i in range(N-1):
  a,b=map(int,input().split())
  G[a].append(b)
  G[b].append(a)
  
def bfs(s):
    seen = [0 for i in range(N+1)]
    d = [0 for i in range(N+1)]
    todo = deque()
    seen[s]=1
    todo.append(s)
    while 1:
      if len(todo)==0:break
      a = todo.popleft()
      for b in G[a]:
        if seen[b] == 0:
          seen[b] = 1
          todo.append(b)
          d[b] += d[a] + 1
    return d
  
d_f = bfs(1)
d_s = bfs(N)

count_f,count_s=0,0
for i in range(1,N+1):
  if d_f[i] <= d_s[i]:count_f +=1
  else: count_s += 1
    
if count_f>count_s:print('Fennec')
else:print('Snuke')
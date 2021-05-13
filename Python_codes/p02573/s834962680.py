from collections import deque
n,m=map(int,input().split())
f=[[] for i in range(n)]
for i in range(m):
  a,b=map(int,input().split())
  a-=1
  b-=1
  f[a].append(b)
  f[b].append(a)
q=deque()

for i in range(n):
  for j in f[i]:
    q.append(j)
  while q:
    p=q.popleft()
    if i!=p:
      f[i]+=f[p]
      for k in f[p]:
        q.append(k)
      f[p]=[]
ans=1
for i in f:
  cnt=len(list(set(i)))
  ans=max(cnt,ans)
print(ans)
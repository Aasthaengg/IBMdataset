from collections import deque
n=int(input())
e=[[]for _ in range(n+1)]
c=[-1]*(n+1)
for _ in range(n-1):
  a,b,w=map(int,input().split())
  e[a]+=[(b,w)]
  e[b]+=[(a,w)]
q=deque([1])
c[1]=0
while q:
  now=q.popleft()
  for to,w in e[now]:
    if c[to]==-1:
      c[to]=(c[now]+w)%2
      q.append(to)
print(*c[1:],sep='\n')
from collections import deque

N=int(input())

G=[[] for _ in range(N+1)]

for _ in range(N-1):
  a,b=map(int,input().split())
  G[a].append(b)
  G[b].append(a)

c=list(map(int,input().split()))
c.sort(reverse=True)

ans=0 
used=[0]*(N+1)
number=[0]*(N+1)
que=deque([1])

ccount=0
while que:
  v=que.popleft()
  if number[v]==0:
    number[v]=c[ccount]
    ccount+=1
  for e in G[v]:
    if used[e]:
      continue
    if number[e]==0:
      number[e]=c[ccount]
      ccount+=1
    ans+=min(number[v],number[e])
    que.append(e)
    used[v]=1
print(ans)
print(*number[1:])
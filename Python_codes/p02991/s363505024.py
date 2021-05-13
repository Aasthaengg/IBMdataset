from collections import deque
n,m=map(int,input().split())
path=[[] for i in range(n*3+3)]
seen=[0]*(3*n)
for i in range(m):
  u,v=map(int,input().split())
  path[3*(u-1)].append(3*(v-1)+1)
  path[3*(u-1)+1].append(3*(v-1)+2)
  path[3*(u-1)+2].append(3*(v-1))
s,t=map(int,input().split())
s-=1
t-=1
q=deque()
q.append(s*3)
seen[s*3]=1
while q:
  x=q.popleft()
  if x%3==0 and x//3==t:
    print(seen[x]//3)
    exit()
  for i in path[x]:
    if seen[i]==0:
      seen[i]=seen[x]+1
      q.append(i)
print(-1)
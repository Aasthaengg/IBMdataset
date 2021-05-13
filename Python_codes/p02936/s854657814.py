N,Q=list(map(int,input().split()))
l=[[] for i in range(N)]
for i in range(N-1):
   a,b=list(map(int,input().split()))
   l[a-1].append(b-1)
   l[b-1].append(a-1)
l_c=[0]*N
for i in range(Q):
   a,b=list(map(int,input().split()))
   l_c[a-1]+=b
visited=[0]*N
from collections import deque
def ans(start):
   que=deque([start])
   visited[start]=1
   while que:
      node=que.popleft()
      for i in l[node]:
         if visited[i]==0:
            l_c[i]+=l_c[node]
            que.append(i)
            visited[i]=1
ans(0)
print(*l_c)
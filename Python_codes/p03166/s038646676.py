n,m=map(int,input().split())
es=[[] for _ in range(n)]
for i in range(m):
    x,y=map(int,input().split())
    es[x-1].append(y-1)

connected=[0]*n
for i in range(n):
    for e in es[i]:
        connected[e]+=1

from collections import deque
que=deque([])
for i in range(n):
    if connected[i]==0:
        que.append(i)
dp=[0]*n

while que:
    s=que.popleft()
    for e in es[s]:
        connected[e]-=1
        dp[e]=max(dp[e], dp[s]+1)
        if connected[e]==0:
            que.append(e)
print(max(dp))
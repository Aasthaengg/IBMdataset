N,M=map(int,input().split())
graph=[[]for _ in range(N)]
deg=[0]*N
for i in range(M):
    xx,yy=map(int,input().split())
    graph[xx-1].append(yy-1)
    deg[yy-1]+=1

que=[]
dp=[0]*N

for i in range(N):
    if deg[i]==0:
        que.append(i)
while len(que)>0:
    k=que.pop(0)
    for x in graph[k]:
        deg[x]-=1
        if deg[x]==0:
            que.append(x)
            dp[x]=max(dp[x],dp[k]+1)
print(max(dp))

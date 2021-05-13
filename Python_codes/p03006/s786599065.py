from collections import deque
n=int(input())
ans=10**18
xy=[list(map(int,input().split())) for _ in range(n)]
d=dict()
for i in range(n):
    a,b=xy[i]
    d[(a,b)]=i
def bfs(s,p,q,visited):
    queue=deque([s])
    visited[s]=1
    while queue:
        x=queue.popleft()
        a,b=xy[x]
        if (a+p,b+q) in d:
            idx=d[(a+p,b+q)]
            if visited[idx]==0:
                visited[idx]=1
                queue.append(idx)
        if (a-p,b-q) in d:
            idx=d[(a-p,b-q)]
            if visited[idx]==0:
                visited[idx]=1
                queue.append(idx)
for i in range(n-1):
    ai,bi=xy[i]
    for j in range(i+1,n):
        aj,bj=xy[j]
        p,q=ai-aj,bi-bj
        cnt=0
        visited=[0]*n
        for k in range(n):
            if visited[k]==0:
                bfs(k,p,q,visited)
                cnt+=1
        ans=min(ans,cnt)
if n==1:
    ans=1
print(ans)
#print(d)
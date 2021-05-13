N,X,Y=map(int,input().split())

G=[[i+1] for i in range(N)]
G[N-1].pop()
for i in range(1,N):
    G[i].append(i-1)
G[X-1].append(Y-1)
G[Y-1].append(X-1)

from collections import deque

q=deque([])
cnt=[0]*N

for n in range(N-1):
    seen=[0]*N
    q.append([n,0])
    seen[n]=1
    while q:
        x,c=q.popleft()
        if c>=N-1:continue
        for g in G[x]:
            if seen[g]==0:
                q.append([g,c+1])
                seen[g]=1
                if n<g:
                    cnt[c+1]+=1
for i in range(1,N):
    print(cnt[i])

import sys
from collections import deque

H,W=map(int,input().split())
S=list(sys.stdin)

ans=0
for i in range(H):
    for j in range(W):
        if S[i][j]=='#':
            continue
        dist=[[-1]*W for _ in range(H)]
        dist[i][j]=0
        que=deque()
        que.append((i,j))
        while que:
            i,j=que.popleft()
            ans=max(ans,dist[i][j])
            for ni,nj in (i-1,j),(i,j+1),(i+1,j),(i,j-1):
                if not (0<=ni<H and 0<=nj<W):
                    continue
                if S[ni][nj]=='#' or dist[ni][nj]!=-1:
                    continue
                dist[ni][nj]=dist[i][j]+1
                que.append((ni,nj))

print(ans)

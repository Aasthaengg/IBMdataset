from collections import deque
H,W = map(int,input().split())
S = [input().strip() for _ in range(H)]
dist = [[-1 for _ in range(W)] for _ in range(H)]
que = deque([(0,0,0)])
dist[0][0] = 0
while que:
    i,j,d = que.popleft()
    if j+1<W and S[i][j+1]=="." and dist[i][j+1]<0:
        dist[i][j+1] = d+1
        que.append((i,j+1,d+1))
    if i-1>=0 and S[i-1][j]=="." and dist[i-1][j]<0:
        dist[i-1][j]=d+1
        que.append((i-1,j,d+1))
    if j-1>=0 and S[i][j-1]=="." and dist[i][j-1]<0:
        dist[i][j-1]=d+1
        que.append((i,j-1,d+1))
    if i+1<H and S[i+1][j]=="." and dist[i+1][j]<0:
        dist[i+1][j]=d+1
        que.append((i+1,j,d+1))
dmin = dist[H-1][W-1]
if dmin<0:
    print(-1)
else:
    B = H*W-dmin-1
    cnt = 0
    for i in range(H):
        for j in range(W):
            if S[i][j]=="#":
                cnt += 1
    print(B-cnt)
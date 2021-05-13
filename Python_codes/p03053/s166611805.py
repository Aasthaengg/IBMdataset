from collections import deque
H,W = map(int,input().split())
A = [input().strip() for _ in range(H)]
B = [[0 for _ in range(W)] for _ in range(H)]
que = deque([])
for i in range(H):
    for j in range(W):
        if A[i][j]=="#":
            que.append((i,j,0))
            B[i][j] = 1
dmax = 0
while que:
    i,j,d = que.popleft()
    if j+1<W and B[i][j+1]==0:
        B[i][j+1]=d+1
        dmax = max(dmax,d+1)
        que.append((i,j+1,d+1))
    if i-1>=0 and B[i-1][j]==0:
        B[i-1][j]=d+1
        dmax = max(dmax,d+1)
        que.append((i-1,j,d+1))
    if j-1>=0 and B[i][j-1]==0:
        B[i][j-1]=d+1
        dmax = max(dmax,d+1)
        que.append((i,j-1,d+1))
    if i+1<H and B[i+1][j]==0:
        B[i+1][j]=d+1
        dmax = max(dmax,d+1)
        que.append((i+1,j,d+1))
print(dmax)
from collections import deque
INFTY = 10000
H,W = map(int,input().split())
S = [input().strip() for _ in range(H)]
A = [[-1 for _ in range(W)] for _ in range(H)]
cnt = 0
for i in range(H):
    for j in range(W):
        if S[i][j]=="#":
            A[i][j]=INFTY
            cnt += 1
que = deque([(0,0,0)])
A[0][0] = 0
while que:
    i,j,d = que.popleft()
    if j+1<W and A[i][j+1]<0:
        A[i][j+1]=d+1
        que.append((i,j+1,d+1))
    if i-1>=0 and A[i-1][j]<0:
        A[i-1][j]=d+1
        que.append((i-1,j,d+1))
    if j-1>=0 and A[i][j-1]<0:
        A[i][j-1]=d+1
        que.append((i,j-1,d+1))
    if i+1<H and A[i+1][j]<0:
        A[i+1][j] = d+1
        que.append((i+1,j,d+1))
if A[H-1][W-1]<0:
    print(-1)
else:
    print(H*W-cnt-A[H-1][W-1]-1)
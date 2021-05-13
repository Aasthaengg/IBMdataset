from collections import deque
H,W = map(int,input().split())
A = [input().strip() for _ in range(H)]
B = [[0 for _ in range(W)] for _ in range(H)]
que = []
for i in range(H):
    for j in range(W):
        if A[i][j]=="#":
            que.append((i,j,0))
que = deque(que)
while que:
    y,x,d = que.popleft()
    if x+1<W and A[y][x+1]=="." and B[y][x+1]==0:
        B[y][x+1]=d+1
        que.append((y,x+1,d+1))
    if y-1>=0 and A[y-1][x]=="." and B[y-1][x]==0:
        B[y-1][x]=d+1
        que.append((y-1,x,d+1))
    if x-1>=0 and A[y][x-1]=="." and B[y][x-1]==0:
        B[y][x-1]=d+1
        que.append((y,x-1,d+1))
    if y+1<H and A[y+1][x]=="." and B[y+1][x]==0:
        B[y+1][x]=d+1
        que.append((y+1,x,d+1))
bmax = 0
for i in range(H):
    for j in range(W):
        bmax = max(bmax,B[i][j])
print(bmax)
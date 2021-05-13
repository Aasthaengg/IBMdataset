from collections import deque
H,W = map(int,input().split())
S = [input().strip() for _ in range(H)]
hist = [[0 for _ in range(W)] for _ in range(H)]
col = 1
for i in range(H):
    for j in range(W):
        if hist[i][j]==0:
            hist[i][j]=col
            que = deque([(i,j,S[i][j])])
            while que:
                y,x,c = que.popleft()
                if x+1<W and S[y][x+1]!=c and hist[y][x+1]==0:
                    hist[y][x+1]=col
                    que.append((y,x+1,S[y][x+1]))
                if y-1>=0 and S[y-1][x]!=c and hist[y-1][x]==0:
                    hist[y-1][x]=col
                    que.append((y-1,x,S[y-1][x]))
                if x-1>=0 and S[y][x-1]!=c and hist[y][x-1]==0:
                    hist[y][x-1]=col
                    que.append((y,x-1,S[y][x-1]))
                if y+1<H and S[y+1][x]!=c and hist[y+1][x]==0:
                    hist[y+1][x]=col
                    que.append((y+1,x,S[y+1][x]))
            col += 1
C = {}
for i in range(H):
    for j in range(W):
        col = hist[i][j]
        if col not in C:
            C[col] = [0,0]
        C[col][0] += 1
        if S[i][j]=="#":
            C[col][1] += 1
cnt = 0
for col in C:
    if col!=0:
        tot = C[col][0]
        x = C[col][1]
        cnt += x*(tot-x)
print(cnt)
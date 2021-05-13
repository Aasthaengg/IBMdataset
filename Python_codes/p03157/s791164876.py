from collections import deque
H,W = map(int,input().split())
S = [input().strip() for _ in range(H)]
D = {0:".",1:"#"}
G = {}
C = {}
hist = [[-1 for _ in range(W)] for _ in range(H)]
col = -1
for i in range(H):
    for j in range(W):
        if S[i][j]=="#" and hist[i][j]==-1:
            col += 1
            G[col] = [(i,j)]
            que = deque([(i,j,1)])
            hist[i][j] = col
            cnt = 0
            while que:
                y,x,a = que.popleft()
                if x+1<W and S[y][x+1]==D[1-a]:
                    if a==1 and hist[y][x+1]!=col:
                        cnt += 1
                        que.append((y,x+1,1-a))
                        hist[y][x+1]=col
                    elif a==0 and hist[y][x+1]==-1:
                        G[col].append((y,x+1))
                        que.append((y,x+1,1-a))
                        hist[y][x+1]=col
                if y-1>-1 and S[y-1][x]==D[1-a]:
                    if a==1 and hist[y-1][x]!=col:
                        cnt += 1
                        que.append((y-1,x,1-a))
                        hist[y-1][x]=col
                    elif a==0 and hist[y-1][x]==-1:
                        G[col].append((y-1,x))
                        que.append((y-1,x,1-a))
                        hist[y-1][x]=col
                if x-1>-1 and S[y][x-1]==D[1-a]:
                    if a==1 and hist[y][x-1]!=col:
                        cnt += 1
                        que.append((y,x-1,1-a))
                        hist[y][x-1]=col
                    elif a==0 and hist[y][x-1]==-1:
                        G[col].append((y,x-1))
                        hist[y][x-1]=col
                        que.append((y,x-1,1-a))
                if y+1<H and S[y+1][x]==D[1-a]:
                    if a==1 and hist[y+1][x]!=col:
                        cnt += 1
                        que.append((y+1,x,1-a))
                        hist[y+1][x]=col
                    elif a==0 and hist[y+1][x]==-1:
                        G[col].append((y+1,x))
                        que.append((y+1,x,1-a))
                        hist[y+1][x]=col
            C[col] = cnt
tot = 0
for col in G:
    tot += len(G[col])*C[col]
print(tot)
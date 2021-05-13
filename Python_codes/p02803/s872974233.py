from collections import deque
INFTY = 10**3
H,W = map(int,input().split())
S = [input().strip() for _ in range(H)]
cmax = 0
for x in range(H):
    for y in range(W):
        if S[x][y]==".":
            A = [[INFTY for _ in range(W)] for _ in range(H)]
            hist = {(i,j):0 for i in range(H) for j in range(W)}
            que = deque([(x,y,0)])
            A[x][y] = 0
            hist[(x,y)] = 1
            while que:
                i,j,d = que.popleft()
                if j+1<W and S[i][j+1]=="." and hist[(i,j+1)]==0:
                    A[i][j+1]=d+1
                    hist[(i,j+1)]=1
                    que.append((i,j+1,d+1))
                if i-1>=0 and S[i-1][j]=="." and hist[(i-1,j)]==0:
                    A[i-1][j]=d+1
                    hist[(i-1,j)]=1
                    que.append((i-1,j,d+1))
                if j-1>=0 and S[i][j-1]=="." and hist[(i,j-1)]==0:
                    A[i][j-1]=d+1
                    hist[(i,j-1)]=1
                    que.append((i,j-1,d+1))
                if i+1<H and S[i+1][j]=="." and hist[(i+1,j)]==0:
                    A[i+1][j]=d+1
                    hist[(i+1,j)]=1
                    que.append((i+1,j,d+1))
            cnt=0
            for i in range(H):
                for j in range(W):
                    if S[i][j]==".":
                        cnt = max(cnt,A[i][j])
            cmax = max(cmax,cnt)
print(cmax)
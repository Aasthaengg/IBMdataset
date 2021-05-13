from collections import deque
H,W,K=map(int,input().split())
s=[list(input()) for i in range(H)]
ans=[[0 for j in range(W)] for i in range(H)]
q=deque([])
cnt=1
for i in range(H):
    for j in range(W):
        if s[i][j]=="#":
            ans[i][j]=cnt
            cnt+=1
            q.appendleft((i,j))
while(len(q)>0):
    x,y=q.popleft()
    if 0<y:
        if ans[x][y-1]==0:
            q.append((x,y-1))
            ans[x][y-1]=ans[x][y]
    if y<W-1:
        if ans[x][y+1]==0:
            q.append((x,y+1))
            ans[x][y+1]=ans[x][y]
for i in range(H):
    if ans[i][0]!=0:
        q.append(i)
while(len(q)>0):
    k=q.popleft()
    if 0<k:
        if ans[k-1][0]==0:
            for j in range(W):
                ans[k-1][j]=ans[k][j]
            q.append(k-1)
    if k<H-1:
        if ans[k+1][0]==0:
            for j in range(W):
                ans[k+1][j]=ans[k][j]
            q.append(k+1)
for line in ans:
    print(*line)

        

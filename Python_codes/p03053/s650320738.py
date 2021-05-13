from collections import deque
def mbfs(S,H,W,d):
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    while(len(d)!=0):
        h=d[0][0]
        w=d[0][1]
        x=d[0][2]
        d.popleft()
        for di in range(4):
            nh=h+dx[di]
            nw=w+dy[di]
            if(nh>H-1 or nh<0 or nw>W-1 or nw<0):
                continue
            if(S[nh][nw]=='#'):
                continue
            S[nh][nw]='#'
            d.append([nh,nw,x+1])
    return x
H,W=map(int,input().split())
A=[list(input()) for i in range(H)]
d=deque()
for i in range(H):
    for j in range(W):
        if(A[i][j]=='#'):
            d.append([i,j,0])
print(mbfs(A,H,W,d))

from collections import deque
def bfs(S,H,W,sh,sw):
    black,white=0,0
    d=deque()
    d.append([sh,sw])
    if S[sh][sw]=='#':
        black+=1
    elif S[sh][sw]=='.':
        white+=1
    seen[sh][sw]=1
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    while(len(d)!=0):
        h=d[0][0]
        w=d[0][1]
        d.popleft()
        for dir in range(4):
            nh=h+dx[dir]
            nw=w+dy[dir]
            if(nh>H-1 or nh<0 or nw>W-1 or nw<0):
                continue
            if(seen[nh][nw] or S[nh][nw]==S[h][w]):
                continue
            if S[nh][nw]=='#':
                black+=1
            else:
                white+=1
            seen[nh][nw]=1
            d.append([nh,nw])
    return white,black

H,W=map(int,input().split())
G=[list(input()) for i in range(H)]
seen=[[0]*W for i in range(H)]
ans=0

for i in range(H):
    for j in range(W):
        if not seen[i][j]:
            w,b=bfs(G,H,W,i,j)
            ans+=w*b
print(ans)
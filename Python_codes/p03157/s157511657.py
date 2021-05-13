H,W=map(int,input().split())
S=[[int(c=='#') for c in input()] for i in range(H)]
v=[[0]*W for i in range(H)]
r=0
def bfs(p,x,y,c,b):
    while 1:
        c^=1
        q=set()
        for h,w in p:
            v[h][w]=1
            if h>0 and not v[h-1][w] and S[h-1][w]==c:
                q.add((h-1,w))
            if w>0 and not v[h][w-1] and S[h][w-1]==c:
                q.add((h,w-1))
            if h<H-1 and not v[h+1][w] and S[h+1][w]==c:
                q.add((h+1,w))
            if w<W-1 and not v[h][w+1] and S[h][w+1]==c:
                q.add((h,w+1))
        if not q:
            return x*y
        if b:
            x+=len(q)
        else:
            y+=len(q)
        b^=1
        p=q
for h in range(H):
    for w in range(W):
        if v[h][w]==0:
            r+=bfs([(h,w)],1,0,S[h][w],0)
print(r)
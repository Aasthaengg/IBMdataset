from collections import deque
H,W=map(int,input().split())
A= [list(input()) for _ in range(H)]
d= [[2000 for _ in range(W)] for _ in range(H)]
move= [ (0,1),(0,-1),(1,0),(-1,0) ]
z= [[False for _ in range(W)] for _ in range(H)]
ans=0

v=deque([])
for i in range(H):
    for j in range(W):
        if A[i][j]=="#":
            v.append( [i,j] )
            z[i][j]=True
            d[i][j]=0
while v:
    a=v.popleft()
    #print(a,v)
    for mv in move:
        s=a[0]+mv[0]
        t=a[1]+mv[1]
        if 0<=s<H and 0<=t<W:
            if z[s][t]==False:
                z[s][t]=True
                d[s][t]=d[a[0]][a[1]]+1
                v.append([s,t])
                ans=max(ans,d[s][t])
#print(d)
print(ans)
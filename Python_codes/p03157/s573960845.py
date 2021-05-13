from collections import deque
H,W=map(int,input().split())
table=[list(input()) for _ in range(H)]
dp=[[-1 for _ in range(W)] for _ in range(H)]
seen=[[0 for _ in range(W)] for _ in range(H)]
d=deque()
col=0
wlist=[0]*(H*W)
blist=[0]*(H*W)
for i in range(H):
    for j in range(W):
        if dp[i][j]==-1:
            col = i*W+j
            d.append([i,j])
            seen[i][j]=1
        while len(d)>0:
            v=d.popleft()
            x=v[0]
            y=v[1]
            dp[x][y]=col
            if x!=0:
                if (table[x][y]!=table[x-1][y])and(seen[x-1][y]==0):
                    seen[x-1][y]=1
                    d.append([x-1,y])
            if x!=H-1:
                if (table[x][y]!=table[x+1][y])and(seen[x+1][y]==0):
                    seen[x+1][y]=1
                    d.append([x + 1, y])
            if y!=0:
                if (table[x][y]!=table[x][y-1])and(seen[x][y-1]==0):
                    seen[x][y-1]=1
                    d.append([x, y-1])
            if y!=W-1:
                if (table[x][y]!=table[x][y+1])and(seen[x][y+1]==0):
                    seen[x][y+1]=1
                    d.append([x, y+1])
            #print(dp)
            #print(d)
            #input()
for i in range(H):
    for j in range(W):
        if table[i][j]=="#":
            blist[dp[i][j]]+=1
        else:
            wlist[dp[i][j]] += 1
#print(wlist,blist)
cnt=0
for i in range(H*W):
    cnt=cnt+blist[i]*wlist[i]
print(cnt)
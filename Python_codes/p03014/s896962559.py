h,w=map(int,input().split())
grid=[]
for _ in range(h):
    s=input()
    g=[0 if i=='#' else 1 for i in s]
    grid.append(g)
toL=[]
toR=[]
toU=[]
toD=[]
for i in range(h):
    tmpL=[]
    tmpR=[]
    tmpU=[]
    tmpD=[]
    for j in range(w):
        if grid[i][j]==0:
            tmpU.append(0)
        elif i==0:
            tmpU.append(1)
        else:
            tmpU.append(toU[i-1][j]+1)
        if grid[-i-1][j]==0:
            tmpD.append(0)
        elif i==0:
            tmpD.append(1)
        else:
            tmpD.append(toD[i-1][j]+1)
        if grid[i][j]==0:
            tmpL.append(0)
        elif j==0:
            tmpL.append(1)
        else:
            tmpL.append(tmpL[-1]+1)
        if grid[i][-j-1]==0:
            tmpR.append(0)
        elif j==0:
            tmpR.append(1)
        else:
            tmpR.append(tmpR[-1]+1)
    toL.append(tmpL)
    toR.append(tmpR[::-1])
    toU.append(tmpU)
    toD.append(tmpD)
toD=toD[::-1]
ans=0
for i in range(h):
    for j in range(w):
        ans=max(ans, toU[i][j]+toD[i][j]+toR[i][j]+toL[i][j]-3)
print(ans)
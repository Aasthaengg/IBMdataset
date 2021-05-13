H,W=map(int,input().split())
L=[list(input())for i in range(H)]
#print(L)

P=[i for i in range(H*W)]
size=[[0,0]for i in range(H*W)]

for i in range(H):
    for j in range(W):
        if L[i][j]==".":
            size[i*W+j][0]+=1
        else:
            size[i*W+j][1]+=1
#print(size)

def find(z):
    if  z==P[z]:
        return z
    else:
        return find(P[z])
def union(x,y):
    X=find(x)
    Y=find(y)
    if sum(size[X])>=sum(size[Y]):
        P[Y]=P[X]
        size[X][0]+=size[Y][0]
        size[X][0]+=size[Y][1]
    else:
        P[X]=P[Y]
        size[Y][0]+=size[X][0]
        size[Y][0]+=size[X][1]
        
for i in range(H):
    for j in range(W):
        if j+1<=W-1:
            
            if L[i][j]!=L[i][j+1]:
                
                if find(i*W+j)!=find(i*W+j+1):
                    #print(i,j)
                    union(i*W+j,i*W+j+1)
        if i+1<=H-1:
            if L[i][j]!=L[i+1][j]:
                if find((i)*W+j)!=find((i+1)*W+j):
                    union(i*W+j,(i+1)*W+j)
BW=[[0,0]for i in range(H*W)]
for i in range(H):
    for j in range(W):
        if L[i][j]==".":
            BW[find(i*W+j)][0]+=1
        else:
            BW[find(i*W+j)][1]+=1

ans=0
for i in range(H):
    for j in range(W):
        if P[i*W+j]==i*W+j:
            ans+=BW[i*W+j][0]*BW[i*W+j][1]
#print(P)
#print(BW)
print(ans)
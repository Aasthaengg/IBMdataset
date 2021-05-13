N,C=map(int,input().split())
D=[list(map(int,input().split())) for i in range(C)]
c=[list(map(int,input().split())) for i in range(N)]

col=[[0 for i in range(C+1)] for j in range(3)]

for i in range(N):
    for j in range(N):
        col[(i+j+2)%3][c[i][j]]+=1

#print(col)

ans=10**15
import itertools
PRD=list(itertools.product([i for i in range(C)], repeat=3))

for i in range(len(PRD)):
    newc=[PRD[i][0],PRD[i][1],PRD[i][2]]
    if newc[0]==newc[1] or newc[1]==newc[2] or newc[2]==newc[0]:
        continue
    cost=0
    for j in range(3):
        for k in range(C):
            cost+=col[j][k+1]*D[k][newc[j]]
    ans=min(cost,ans)

print(ans)
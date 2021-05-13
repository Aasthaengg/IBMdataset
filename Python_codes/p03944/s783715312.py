import itertools

W,H,N=map(int,input().split())
xya=[list(map(int,input().split())) for i in range(N)]
res=[[True for j in range(H)] for i in range(W)]
for j in range(H):
    for i in range(W):
        for k in range(N):
            if (i<xya[k][0] and xya[k][2]==1) or (i>=xya[k][0] and xya[k][2]==2) or (j<xya[k][1] and xya[k][2]==3) or (j>=xya[k][1] and xya[k][2]==4):
                res[i][j]=False
                break
res2=list(itertools.chain.from_iterable(res))

print(res2.count(True))

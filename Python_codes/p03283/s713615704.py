N,M,Q=map(int, input().split())

L=[[0]*N for _ in range(N)]
for i in range(M):
    l,r=map(int, input().split())
    L[l-1][r-1]+=1

for i in range(N):
    for j in range(N):
        if i==0 and j==0:
            continue
        elif i==0:
            L[i][j]+=L[i][j-1]
        elif j==0:
            L[i][j]+=L[i-1][j]
        else:
            L[i][j]+=L[i-1][j]+L[i][j-1]-L[i-1][j-1]


#print(L)
for i in range(Q):
    p,q=map(int, input().split())
    p-=1
    q-=1
    if p==0:
        print(L[q][q])
    else:
        print(L[q][q]-L[p-1][q]-L[q][p-1]+L[p-1][p-1])
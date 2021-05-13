N,M,Q=map(int,input().split())
x=[[0]*N for i in range(N)]
for i in range(M):
    L,R=map(lambda x:int(x)-1,input().split())
    x[L][R]+=1
cum=[[0]*(N+1) for i in range(N+1)]
for l in range(N):
    for r in range(N):
        cum[l][r+1]=cum[l][r]+x[l][r]
for i in range(Q):
    p,q=map(lambda x:int(x)-1,input().split())
    res=0
    for l in range(p,q+1):
        res+=cum[l][q+1]-cum[l][p]
    print(res)
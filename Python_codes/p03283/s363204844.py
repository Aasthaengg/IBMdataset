N,M,Q=list(map(int,input().split()))
t=[list(map(int,input().split())) for _ in range(M)]
query=[list(map(int,input().split())) for _ in range(Q)]

train=[[0]*(N+1) for _ in range(N+1)]
c=[[0]*(N+1) for _ in range(N+1)]

for l,r in t:
    train[l][r]+=1

for l in range(1,N+1):
    for r in range(1,N+1):
        c[l][r]=c[l][r-1]+train[l][r]

for p,q in query:
    tmp=0
    for l in range(p,q+1):
        tmp+=c[l][q]-c[l][p-1]
    
    print(tmp)
N,M=map(int,input().split())

S=[[] for _ in range(N+1)]
for i in range(M):
    T=list(map(int,input().split()))
    for x in T[1:]:
        S[x].append(i+1)

P=["*"]+list(map(int,input().split()))

X=0
for i in range(2**N):
    Q=["*"]+[0]*M
    for x in range(N):
        if i%2:
            for k in S[x+1]:
                Q[k]=(Q[k]+1)%2
                
        i>>=1
    X+=(P==Q)
print(X)

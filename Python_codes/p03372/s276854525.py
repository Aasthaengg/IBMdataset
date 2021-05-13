N,C = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
A.insert(0,[0,0])

F = [0 for _ in range(N+1)]
F[N] = A[N][1]-(C-A[N][0])
for i in range(N-1,0,-1):
    F[i] = F[i+1]+A[i][1]-(A[i+1][0]-A[i][0])
G = [0 for _ in range(N+1)]
for i in range(1,N+1):
    G[i] = G[i-1]+A[i][1]-(A[i][0]-A[i-1][0])
cmax = max(max(F),max(G))
dmax = 0
for i in range(N-1,0,-1):
    dmax = max(dmax,F[i+1])
    cmax = max(cmax,dmax+G[i]-A[i][0])
emax = 0
for i in range(2,N+1):
    emax = max(emax,G[i-1])
    cmax = max(cmax,emax+F[i]-(C-A[i][0]))
print(cmax)
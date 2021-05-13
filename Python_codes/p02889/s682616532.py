INFTY = 10**12
def wf(H):
    d = [[INFTY for _ in range(N+1)] for _ in range(N+1)]
    for i in range(1,N+1):
        d[i][i] = 0
        if i in H:
            for x in H[i]:
                j,c = x[0],x[1]
                d[i][j] = c
    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                d[i][j] = min(d[i][j],d[i][k]+d[k][j])
    return d
N,M,L = map(int,input().split())
G = {}
for _ in range(M):
    A,B,C = map(int,input().split())
    if A not in G:
        G[A] = []
    G[A].append((B,C))
    if B not in G:
        G[B] = []
    G[B].append((A,C))
d1 = wf(G)
F = {}
for i in range(1,N):
    for j in range(i+1,N+1):
        if d1[i][j]<=L:
            if i not in F:
                F[i] = []
            F[i].append((j,1))
            if j not in F:
                F[j] = []
            F[j].append((i,1))
d2 = wf(F)
Q = int(input())
for _ in range(Q):
    s,t = map(int,input().split())
    if d2[s][t]<INFTY:
        print(d2[s][t]-1)
    else:
        print(-1)

H,W = map(int,input().split())
inf=10**10
n=10

e = [[inf]*n for _ in range(n)]

for i in range(10):
    S=list(map(int,input().split()))
    for j in range(10):
        e[i][j]=S[j]





cost=[inf]*10


def dijkstra(s):
    color=["WHITE"]*n
    d=[inf]*n
    p=[-1]*n
    d[s]=0
    p[s]=-1
    while True:
        mincost =inf
        for i in range(n):
            if color[i] !="BLACK" and d[i] < mincost:
                mincost =d[i]
                u=i
        if mincost ==inf:
            break
        color[u]="BLACK"
        
        for v in range(n):
            if color[v] !="BLACK" and e[u][v] !=inf:
                if d[u] +e[u][v] <d[v]:
                    d[v]=d[u] +e[u][v]
                    p[v]=u
                    color[v] ="GRAY"
    return d[1]
ans=10**10

T=[0]*10
for i in range(H):
    S=list(map(int,input().split()))
    for j in range(W):
        if S[j]!=-1:
            T[S[j]]+=1



goukei=0
for i in range(10):
    if i!=1:
        ret=dijkstra(i)

        goukei+=ret*T[i]
print(goukei)
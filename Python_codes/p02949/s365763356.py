import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n,m,p=map(int,input().split())
    E=[[] for _ in range(n)]
    R=[[] for _ in range(n)]
    for _ in range(m):
        u,v,c=map(int,input().split())
        u-=1; v-=1
        E[u].append((v,p-c))
        R[v].append((u,p-c))

    # 0 から到達できる点、N-1 から逆辺で到達できる点を列挙
    state=[0]*n
    state[0]+=1
    state[-1]+=2

    Q=[0]
    while(Q):
        v=Q.pop()
        for nv,w in E[v]:
            if(state[nv]&1): continue
            state[nv]+=1
            Q.append(nv)

    Q=[n-1]
    while(Q):
        v=Q.pop()
        for nv,w in R[v]:
            if(state[nv]&2): continue
            state[nv]+=2
            Q.append(nv)

    # state が 3 の辺だけを用いて Bellman Ford
    dist=[INF]*n
    dist[0]=0
    for k in range(n):
        update=False
        for v in range(n):
            if(state[v]!=3): continue
            for nv,w in E[v]:
                if(state[nv]!=3): continue
                if(dist[nv]>dist[v]+w):
                    dist[nv]=dist[v]+w
                    update=True
        if(not update):
            break
        if(update and k==n-1):
            print(-1)
            return

    print(max(0,-dist[-1]) if(dist[-1]!=INF) else -1)
resolve()
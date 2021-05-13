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

    # 0 から到達できる点、かつ n-1 から逆辺で到達できる点を計算
    state=[0]*n
    state[0]+=1
    state[n-1]+=2

    # from 0
    Q=[0]
    while(Q):
        v=Q.pop()
        for nv,w in E[v]:
            if(state[nv]&1): continue
            state[nv]+=1
            Q.append(nv)

    # to n-1
    Q=[n-1]
    while(Q):
        v=Q.pop()
        for nv,w in R[v]:
            if(state[nv]&2): continue
            state[nv]+=2
            Q.append(nv)

    # state[v]==3 を結ぶ頂点のみを用いてBellman-Ford
    dist=[INF]*n
    dist[0]=0
    for k in range(n):
        flag=0
        for v in range(n):
            for nv,w in E[v]:
                if(state[v]&state[nv]!=3): continue
                if(dist[nv]>dist[v]+w):
                    dist[nv]=dist[v]+w
                    flag=1
        if(flag and k==n-1):
            print(-1)
            return

    print(max(-dist[-1],0))
resolve()
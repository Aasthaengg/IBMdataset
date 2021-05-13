def dist_bfs(N,E,start):
    d = [-1]*N
    d[start] = 0
    q = [start]
    while q:
        qq = []
        for i in q:
            di = d[i]
            for j in E[i]:
                if d[j]!=-1:continue
                d[j] = di+1
                q.append(j)
        q = qq
    return d

N,M = map(int,input().split())
UV = [list(map(int,input().split())) for _ in [0]*M]
S,T = map(int,input().split())

S-=1;T-=1
E = [[] for _ in [0]*3*N]
for u,v in UV:
    u-=1;v-=1
    for i in range(3):
        v = (v+N)%(3*N)
        E[u+i*N].append(v)

print(dist_bfs(3*N,E,S)[T]//3)
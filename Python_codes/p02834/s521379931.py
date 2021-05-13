def solve(N,u,v,G):
    
    def ikisaki(u):
        U = [0]*(N+1)
        u_que = [[u,0,-1]]
        u_visited = [0]*(N+1)
        u_visited[u] = 1
        while u_que != []:
            now,kaisuu,parent = u_que.pop()
            for to in G[now]:
                if to != parent:
                    U[to] = kaisuu+1
                    if len(G[to])!=1:
                        u_que.append([to,kaisuu+1,now])
        return U
    V = ikisaki(v)
    U = ikisaki(u)
    
    maxV = 0
    for i in range(1,N+1):
        if V[i] > U[i]:
            maxV = max(maxV,V[i])
    print(maxV-1)
    

    

N,u,v = map(int,input().split())
from collections import defaultdict
G = defaultdict(list)
for i in range(N-1):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)

solve(N,u,v,G)
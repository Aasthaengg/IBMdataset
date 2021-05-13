MAX_D = 10**9
def solve():
    N,M = map(int, input().split())
    d = [[MAX_D]*N for _ in range(N)]
    edges = [[False]*N for _ in range(N)]
    base_edge = {}
    for _ in range(M):
        a,b,c = map(int, input().split())
        edges[a-1][b-1] = True
        edges[b-1][a-1] = True
        d[a-1][b-1] = c
        d[b-1][a-1] = c
        base_edge[(a-1,b-1)] = c
        base_edge[(b-1,a-1)] = c
        
    # ワーシャルフロイド法
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i != j and d[i][j] > d[i][k]+d[k][j]:
                    # print(i+1,k+1,j+1, d[i][j], d[i][k], d[k][j])
                    edges[i][j] = False
                    if (i,k) in base_edge and base_edge[(i,k)] == d[i][k]: edges[i][k] = True
                    if (k,j) in base_edge and base_edge[(k,j)] == d[k][j]: edges[k][j] = True
                    d[i][j] = d[i][k]+d[k][j]
                    
    # print(edges)
    print(M - sum(map(sum, edges))//2)
    
solve()
inf = float('inf')

def solve():
    N, M = map(int, input().split())
    edges = [None] * M

    for i in range(M):
        a, b, c = map(int, input().split())
        a, b = a-1, b-1
        edges[i] = (a, b, -c)

    ans = BellmanFord(N, M, edges)
    if ans is None:
        print('inf')
    else:
        print(-ans)

def BellmanFord(N, M, edges):
    d = [inf] * N
    d[0] = 0

    for i in range(N-1):
        for(u, v, c) in edges:
            if d[u] + c < d[v]:
                d[v] = d[u] + c

    for i in range(N):
        for(u, v, c) in edges:
            if d[u] + c < d[v]:
                d[v] = -inf

    if d[N-1] == -inf:
        return None
    else:
        return d[N-1]
    
if __name__ == '__main__':
    solve()
                
                

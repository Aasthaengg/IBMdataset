def solve():
    H, W = map(int,input().split())
    cost = [list(map(int,input().split())) for _ in range(10)]
    A = [list(map(int,input().split())) for _ in range(H)]
    d = []
    for i in range(10):
        d.append(dijkstra(i,10,cost))
    
    ans = 0
    for h in range(H):
        for w in range(W):
            if A[h][w] != -1:
                ans += d[A[h][w]][1]
    
    print(ans)

def dijkstra(s,N,cost):
    d = [float("inf")] * N
    used = [False] * N
    d[s] = 0

    while True:
        v = -1
        for u in range(N):
            if not used[u] and (v == -1 or d[u] < d[v]):
                v = u
        if v == -1:
            break
        used[v] = True

        for u in range(N):
            d[u] = min(d[u], d[v] + cost[v][u])
    
    return d

if __name__ == '__main__':
    solve()
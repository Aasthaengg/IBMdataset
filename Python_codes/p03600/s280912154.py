INF = 10**18

N = int(input())
G = [list(map(int,input().split())) for _ in range(N)]

# warshall-floyd
dist = [G[i][:] for i in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

ans = 0
for i in range(N):
    for j in range(i+1,N):
        ans += G[i][j]

        if dist[i][j] < G[i][j]:
            print(-1)
            exit()

        for k in range(N):
            if i == k or j == k: continue
            if dist[i][j] == dist[i][k] + dist[k][j]:
                ans -= dist[i][j]
                break
        
print(ans)
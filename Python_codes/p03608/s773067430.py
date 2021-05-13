from itertools import permutations

N, M, R = map(int, input().split())
r = list(map(lambda x: int(x) - 1, input().split()))
d = [[float("inf") for _ in range(N)] for _ in range(N)] 
for i in range(M):
    x, y, z = map(int, input().split())
    d[x-1][y-1] = min(d[x-1][y-1], z)
    d[y-1][x-1] = min(d[x-1][y-1], z)
for i in range(N):
    d[i][i] = 0

def warshall_floyd(d):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

short_dist = warshall_floyd(d)

ans = float('inf')
for ptn in permutations(r):
    dist = 0
    for x, y in zip(ptn, ptn[1:]):
        dist += short_dist[x][y]
    ans = min(ans, dist)
        
print(ans)
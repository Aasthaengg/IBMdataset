from itertools import permutations
n, m, r = map(int, input().split())
INF = 1 << 60

d = [[INF] * n for i in range(n)]
rs = list(map(int, input().split()))

for i in range(m):
    a,b,c = map(int, input().split())
    a -= 1
    b -= 1
    d[a][b] = c
    d[b][a] = c

def warshall_floyd(d):
    """
    input
        d : 初期全点対距離
    output
        d : 最適化後全点対距離
    """
    n = len(d)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k]+d[k][j])
    return d

d_optimized = warshall_floyd(d)
# print(d_optimized)

ans = INF
for inds in permutations([r-1 for r in rs]):
    cnt = 0
    for i in range(r-1):
        prev = inds[i]
        nxt = inds[i+1]
        cnt += d_optimized[prev][nxt]
    ans = min(ans,cnt)
print(ans)
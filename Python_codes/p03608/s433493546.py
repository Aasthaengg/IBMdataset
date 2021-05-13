from itertools import permutations

def warshall_floyd():
    '''
    すべての頂点間の最短距離を求める (重み付き有向グラフ)
    '''
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


n, m, r = map(int, input().split())
city = list(map(int, input().split()))

dist = [[float('inf')] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a-1][b-1] = c
    dist[b-1][a-1] = c
for i in range(n):
    dist[i][i] = 0

warshall_floyd()

res = float('inf')
for l in permutations(range(r), r):
    d = 0
    for i in range(r-1):
        d += dist[city[l[i]]-1][city[l[i+1]]-1]
    res = min(res, d)

print(res)
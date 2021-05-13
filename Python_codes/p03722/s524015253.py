n, m = map(int, input().split())
NMAX = 1000; MMAX = 2000

INF = 10**15

edge = []
for _ in range(m):
    a, b, c = map(int, input().split())
    # 最短距離の問題に変える
    a -= 1; b -= 1; c = -c
    edge.append([a, b, c])

# Bellman-Ford O(NM)
dist = [INF for _ in range(NMAX)] # 頂点1からの最短距離を格納する配列
dist[0] = 0
for loop in range(n):
    for i in range(m):
        a, b, c = edge[i]
        if dist[a] == INF:
            continue
        dist[b] = min(dist[b], dist[a]+c)

ans = dist[n-1]

# 負の閉路検出 O(NM)
## すでにBellman-Fordを実施しているので、distには頂点1から各頂点vまでの最短距離が格納されているはず
## もしまだ更新されるようなら、負の閉路(問題に合わせると正の閉路)が存在していることになる
negative = [False for _ in range(NMAX)] # 頂点iが負の閉路に含まれる場合はTrue
for loop in range(n):
    for i in range(m):
        a, b, c = edge[i]
        if dist[a] == INF:
            continue
        if dist[b] > dist[a]+c:
            dist[b] = dist[a]+c
            negative[b] = True
        if negative[a]:
            negative[b] = True

if negative[n-1]:
    print("inf")
else:
    print(-ans)
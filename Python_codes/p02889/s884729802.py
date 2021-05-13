inf = float('inf')

#計算量O(V^3) V:頂点数
# dist[i][j]: iからjへのコスト,  n:頂点数
def warshall_floyd(ad):
    n = len(ad)
    dist = [line[:] for line in ad]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    dist[i][j] = 0
                elif dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

N, M, L = map(int,input().split())
ad = [[inf] * N for _ in range(N)]
for _ in range(M):
    A, B, C = map(int,input().split())
    if C > L:
        continue
    A -= 1
    B -= 1
    ad[A][B] = C
    ad[B][A] = C
Q = int(input())
query = [[int(e)-1 for e in input().split()] for _ in range(Q)]

ad = warshall_floyd(ad)
for s in range(N):
    for t in range(N):
        if ad[s][t] <= L:
            ad[s][t] = 1
        else:
            ad[s][t] = inf

ad = warshall_floyd(ad)
for s, t in query:
    ans = ad[s][t] - 1
    if ans == inf:
        ans = -1
    print(ans)
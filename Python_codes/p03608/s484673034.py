from itertools import permutations
N, M, R = map(int, input().split())
r = list(map(int, input().split()))
r = permutations(r, len(r))
INF = 10**10
dist = [[INF]*N for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    dist[a-1][b-1] = dist[b-1][a-1] = c
for k in range(N):
    for i in range(N):
        for j in range(N):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] =  dist[j][i] = dist[i][k] + dist[k][j]
ans = INF
for i in r:
    tmp = 0
    for j in range(len(i)-1):
        tmp += dist[i[j]-1][i[j+1]-1]
    ans = min(ans, tmp)
print(ans)
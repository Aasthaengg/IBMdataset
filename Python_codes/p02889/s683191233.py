import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, M, L = mapint()
dist = [[10**18]*N for _ in range(N)]
for _ in range(M):
    a, b, c = mapint()
    dist[a-1][b-1] = c
    dist[b-1][a-1] = c

for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j]=min(dist[i][j], dist[i][k]+dist[k][j])

oil = [[10**18]*N for _ in range(N)]
for i in range(N-1):
    for j in range(i+1, N):
        if dist[i][j]<=L:
            oil[i][j] = 1
            oil[j][i] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            oil[i][j]=min(oil[i][j], oil[i][k]+oil[k][j])

Q = int(input())
for _ in range(Q):
    s, t = mapint()
    if oil[s-1][t-1]>=10**17:
        print(-1)
    else:
        print(oil[s-1][t-1]-1)
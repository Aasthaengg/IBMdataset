def warshall_floyd(d):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d
N, M, R = map(int,input().split())
r = list(map(int,input().split()))
d = [[float("inf")]*N for i in range(N)]
edge = [[] for i in range(N)]
for i in range(M):
    x, y, z = map(int,input().split())
    d[x-1][y-1] = z
    d[y-1][x-1] = z
for i in range(N):
    d[i][i] = 0

warshall_floyd(d)
ans = float('inf')

import itertools
for i in itertools.permutations(r):
    tmp = 0
    for k in range(1,R):
        tmp += d[i[k-1]-1][i[k]-1]
    ans = min(ans,tmp)
print(ans)
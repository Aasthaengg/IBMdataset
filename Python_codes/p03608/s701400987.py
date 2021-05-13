from itertools import permutations
 
N, M, R = map(int, input().split())
r = [a-1 for a in [int(x) for x in input().split()]]
d = [[float("inf")]*N for _ in range(N)]

for i in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    d[a][b] = c
    d[b][a] = c

for a in range(N):
    d[a][a] = 0

res = float("inf")

for k in range(N):
    for i in range(N):
        for j in range(N):
            if d[i][k]+d[k][j] < d[i][j]:
                d[i][j] = d[i][k]+d[k][j]

for p in permutations(r):
    distance = 0
    for i in range(len(p)-1):
        distance += d[p[i]][p[i+1]]
    res = min(distance, res)

print(res)


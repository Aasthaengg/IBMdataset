N,M,R = map(int,input().split())
R = list(map(int,input().split()))
ABC = [tuple(map(int,input().split())) for i in range(M)]

INF = float('inf')
d = [[INF]*N for _ in range(N)]
for i in range(N):
    d[i][i] = 0
for a,b,c in ABC:
    a,b = a-1,b-1
    d[a][b] = d[b][a] = c

for k in range(N):
    for i in range(N):
        for j in range(N):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

ans = INF
import itertools
for ptn in itertools.permutations(R):
    tmp = 0
    for a,b in zip(ptn,ptn[1:]):
        tmp += d[a-1][b-1]
    ans = min(ans, tmp)
print(ans)
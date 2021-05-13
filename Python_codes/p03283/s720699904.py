import sys
input = sys.stdin.readline
N,M,Q = map(int,input().split())
LR = [tuple(map(int,input().split())) for i in range(M)]
PQ = [tuple(map(int,input().split())) for i in range(Q)]

imos = [[0]*(N+1) for _ in range(N+1)]
for l,r in LR:
    imos[l][r] += 1
for i in range(N+1):
    for j in range(N):
        imos[i][j+1] += imos[i][j]
for j in range(N+1):
    for i in range(N):
        imos[i+1][j] += imos[i][j]

ans = []
for p,q in PQ:
    p -= 1
    a = imos[q][q] + imos[p][p] - imos[p][q] - imos[q][p]
    ans.append(a)
print(*ans, sep='\n')
from heapq import *
INF = 1e10

def floyd(n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]

N,M,L = map(int,input().split())

d = [[INF]*N for i in range(N)]

for x in range(M):
    a,b,w = map(int,input().split())
    d[a-1][b-1] = w
    d[b-1][a-1] = w

floyd(N)

grafo2 = [[INF] * N for i in range(N)]

for x in range(N):
    for y in range(N) :
        if d[x][y] <= L:
            grafo2[x][y] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if grafo2[i][j] > grafo2[i][k] + grafo2[k][j]:
                grafo2[i][j] = grafo2[i][k] + grafo2[k][j]

query = int(input())

for x in range(query):
    s,t = map(int,input().split())
    if grafo2[s-1][t-1] == INF:
        print(-1)
    else:
        print(grafo2[s-1][t-1] - 1)

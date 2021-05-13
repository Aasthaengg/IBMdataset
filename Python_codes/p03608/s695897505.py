INF = 10 ** 8
import itertools

N, M, R = map(int, input().split())
r = list(map(int, input().split()))
ABC = []
for _ in range(M):
    ABC.append(tuple(map(int, input().split())))

G = [[INF] * N for _ in range(N)]
for i in range(N):
    G[i][i] = 0
for el in ABC:
    a, b, c = el
    G[a-1][b-1] = c
    G[b-1][a-1] = c

for k in range(N):
    for i in range(N):
        for j in range(N):
            #print(G)
            G[i][j] = min(G[i][k] + G[k][j], G[i][j])

#print(G)
p = itertools.permutations(r)
m = INF
for el in p:
    #print(el)
    dist = 0
    for i in range(R - 1):
        dist += G[el[i] - 1][el[i + 1] - 1]
    m = min(m, dist)
print(m)







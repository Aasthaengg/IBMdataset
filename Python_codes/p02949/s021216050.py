INF = 1e12
n,m,p = map(int,input().split())

grafo = []

for x in range(m):
    a,b,c = map(int,input().split())
    grafo.append((a-1,b-1,c-p))

def bellman_ford(v):
    distancia = [float("inf")] * n
    distancia[v] = 0
    for i in range(2 * n):
        for a,b,c in grafo:
            if distancia[b] > distancia[a] - c:
                distancia[b] = distancia[a] - c
                if i == n - 1:
                    distancia[b] = -float("inf")
    return distancia

distancia = bellman_ford(0)

if distancia[-1] ==  -float("inf"):
    print(-1)
else:
    if distancia[-1] > 0:
        print(0)
    else:
        print(-1 * distancia[-1])

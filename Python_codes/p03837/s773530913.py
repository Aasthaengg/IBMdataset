
INF = 10**19

def dijkstra_back(s,t,n,w,cost):
    prev = [s] * n 
    d = [float("inf")] * n
    used = [False] * n
    d[s] = 0
    
    while True:
        v = -1
        for i in range(n):
            if (not used[i]) and (v == -1):
               v = i
            elif (not used[i]) and d[i] < d[v]:
                v = i
        if v == -1:
               break
        used[v] = True
        
        for i in range(n):
            if d[i] > d[v] + cost[v][i]: 
                d[i] = d[v] + cost[v][i]
                prev[i] = v
    path = [t]
    while prev[t] != s:
        path.append(prev[t])
        prev[t] = prev[prev[t]]
    path.append(s)
    path = path[::-1]
    return path

N,M = map(int, input().split())

cost = [[float("inf") for i in range(N)] for j in range(N)]
edges = set()
for i in range(M):
    a,b,c = map(int, input().split())
    a -= 1
    b -= 1
    cost[a][b] = c
    cost[b][a] = c
    edges.add(min(a,b)*10**5 + max(a,b))

for i in range(N):
    for j in range(i+1,N):
        d = dijkstra_back(i,j,N,M,cost)
        for k in range(len(d)-1):
            a_ = min(d[k],d[k+1])
            b_ = max(d[k],d[k+1])
            X = a_*10**5+b_
            if X in edges:
                edges.remove(X)
print(len(edges))


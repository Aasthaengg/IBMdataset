n, m = map(int,input().split())
adj = [[0]*(n+1) for i in range(n+1)]
edges = []
for i in range(m):
    a, b = map(int, input().split())
    edges.append((a, b))
    adj[a][b] = 1
    adj[b][a] = 1


visited = [False] * (n+1)
parents = [None] * (n+1)
cycles = set()
count = 0
def dfs(u):
    for v in range(n+1):
        if adj[u][v]:
            if parents[u] == v:
                continue
            #print (u, v)
            #print (parents)
            adj[u][v], adj[v][u] = 0, 0
            if parents[v] is not None:
                #print ("Isn't None", u, v, parents[u])
                cycles.add(u)
                cycles.add(v)
                w = parents[u]
                while w != v:
                    cycles.add(w)
                    w = parents[w]
                
            if parents[v] == None: 
                parents[v] = u
                dfs(v)
parents[1] = 0
dfs(1)
ans = m
#print (parents)
for i in range(m):
    a, b = edges[i]
    if a in cycles and b in cycles:
        ans -= 1
print (ans)
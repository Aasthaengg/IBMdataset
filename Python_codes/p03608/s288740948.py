import itertools

n,m,r = map(int,input().split())
R = list(map(int,input().split()))
V = [[] for i in range(n+1)]
for i in range(m):
    a,b,c = map(int,input().split())
    V[a].append([b,c])
    V[b].append([a,c])
    
cost = [[float("Inf") for j in range(n+1)] for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        for v,d in V[i]:
            if v == j:
                cost[i][j] = d

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if cost[i][j] > cost[i][k] + cost[k][j]:
                cost[i][j] = cost[i][k] + cost[k][j]

L = list(itertools.permutations(R, r))
ans = float("Inf")

for x in L:
    p = 0
    for i in range(len(x)-1):
        p += cost[x[i]][x[i+1]]
        
    ans = min(ans, p)
print(ans)
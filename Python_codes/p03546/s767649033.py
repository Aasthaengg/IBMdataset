H,W = list(map(int,input().split()))
V = 10
cost = []
for i in range(V):
    cost.append(list(map(int,input().split())))

INF = float('inf')
for k in range(V):
    for i in range(V):
        for j in range(V):
            if cost[i][k]!=INF and cost[k][j]!=INF:
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

out = 0
for i in range(H):
    A = list(map(int,input().split()))
    for j in range(W):
        if A[j]==-1:
            continue
        else:
            out += cost[A[j]][1]
print(out)
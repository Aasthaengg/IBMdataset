N,M = map(int,input().split())
edges = []
for _ in range(M):
    s,t,d = map(int,input().split())
    edges.append((s,t,d))

cost = [-1*float("INF") for _ in range(N+1)]
cost[1] = 0
count = 0
while count < N:
    count += 1
    for s,t,d in edges:
        if cost[s] + d > cost[t]:
            cost[t] = cost[s] + d
ans = cost[N]

negative = [False]*(N+1)
count = 0
while count <= N:
    count += 1
    for s,t,d in edges:
        if cost[s] + d > cost[t]:
            cost[t] = cost[s] + d
            negative[t] = True
for s,t,d in edges:
        if negative[s]:
            negative[t] = True

if negative[N]:
    print("inf")
else:
    print(ans)
N,M = map(int,input().split())
edges = []
for _ in range(M):
    a,b,c = map(int,input().split())
    edges.append((a,b,c))

cost = [-float("INF")]*(N+1)
cost[1] = 0
cnt = 0
flag = True
for _ in range(N):
    for a,b,c in edges:
        if cost[a]+c > cost[b]:
            cost[b] = cost[a]+c

tmp = cost[N]

for _ in range(N):
    for a,b,c in edges:
        if cost[a]+c > cost[b]:
            cost[b] = cost[a]+c

if tmp < cost[N]:
    print("inf")
else:
    print(tmp)


N,C = map(int,input().split())
D = []
for i in range(C):
    D.append(list(map(int,input().split())))
G = []
for i in range(N):
    G.append(list(map(int,input().split())))

X = [[] for i in range(3)]
for i in range(N):
    for j in range(N):
        X[(i+j+2)%3].append(G[i][j])
ans = float('inf')

Costs = [[0 for i in range(C)] for j in range(3)]

for c in range(C):
    for i in range(3):
        for e in X[i]:
            Costs[i][c] += D[e-1][c]

for c1 in range(C):
    for c2 in range(C):
        if c1 == c2:
            continue
        for c3 in range(C):
            if c1 == c3 or c2 == c3:
                continue
            cost = 0
            for i,e in enumerate([c1,c2,c3]):
                cost += Costs[i][e]
            ans = min(cost,ans)
print(ans)

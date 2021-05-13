N,C = map(int,input().split())
D = [list(map(int,input().split())) for _ in range(C)]

G = [list(map(int,input().split())) for _ in range(N)]
g1 = []
g2 = []
g3 = []
for i in range(N):
    for j in range(N):
        G[i][j] -= 1
        if (i+j)%3 == 0:
            g1.append(G[i][j])
        if (i+j)%3 == 1:
            g2.append(G[i][j])
        if (i+j)%3 == 2:
            g3.append(G[i][j])



cost = [[0]*3 for _ in range(C)]
for c in range(C):
    for g in range(3):
        if g == 0:
            cost[c][0] = sum(D[clr_g1][c] for clr_g1 in g1)
        if g == 1:
            cost[c][1] = sum(D[clr_g2][c] for clr_g2 in g2)
        if g == 2:
            cost[c][2] = sum(D[clr_g3][c] for clr_g3 in g3)



ans = float('inf')
for c1 in range(C):
    for c2 in range(C):
        for c3 in range(C):
            temp = 0
            if c1 == c2 or c2 == c3 or c3 == c1:
                continue
            # temp += sum(D[clr_g1][c1] for clr_g1 in g1)
            # temp += sum(D[clr_g2][c2] for clr_g2 in g2)
            # temp += sum(D[clr_g3][c3] for clr_g3 in g3)
            temp = cost[c1][0] + cost[c2][1] + cost[c3][2]
            ans = min(ans,temp)
print(ans)
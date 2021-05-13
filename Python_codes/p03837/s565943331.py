n, m = map(int, input().split())

DP = [[10**5 for _ in range(n)] for _ in range(n)]
for i in range(n):
    DP[i][i] = 0

Edge = []
for _ in range(m):
    a, b, c = map(int, input().split())
    DP[a-1][b-1] = c
    DP[b-1][a-1] = c
    Edge.append((a,b,c))

for k in range(n):
    for i in range(n):
        for j in range(n):
            DP[i][j] = min(DP[i][j], DP[i][k] + DP[k][j])

Edge_check = [0 for _ in range(len(Edge))]
for e in range(len(Edge)):
    for s in range(n):
        for t in range(n):
            if s == t:
                continue
            i = Edge[e][0] -1
            j = Edge[e][1] -1
            cost = Edge[e][2]
            if DP[s][i] + cost + DP[j][t] == DP[s][t]:
                Edge_check[e] = 1

ans = len(Edge_check) - sum(Edge_check)
print(ans)


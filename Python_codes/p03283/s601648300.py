n, m, q = map(int, input().split())
G = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    l, r = map(int, input().split())
    G[l][r] += 1
for i in range(1, n + 1):
    for j in range(1, n + 1):
        G[i][j] += G[i - 1][j] + G[i][j - 1] - G[i - 1][j - 1]
p = [list(map(int, input().split())) for _ in range(q)]
for u in p:
    s, t = u[0] - 1, u[1]
    print(G[s][s] + G[t][t] - (G[s][t] + G[t][s]))
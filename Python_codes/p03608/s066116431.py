from itertools import combinations, permutations

N, M, R = [int(_) for _ in input().split()]
r_list = [int(_) for _ in input().split()]

INF = 10 ** 9
G = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(M):
    a, b, c = [int(_) for _ in input().split()]
    G[a - 1][b - 1] = c
    G[b - 1][a - 1] = c

for k in range(N):
    for i in range(N):
        for j in range(N):
            G[i][j] = min(G[i][j], G[i][k] + G[k][j])

ans = INF * R
for p in permutations(range(R)):
    val = 0
    for i in range(R - 1):
        c = r_list[p[i]]-1
        n = r_list[p[i + 1]]-1
        val += G[c][n]
    ans = min(ans, val)
print(ans)

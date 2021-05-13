N = int(input())

INF = 10 ** 9 + 7
G = [[int(_) for _ in input().split()] for _ in range(N)]
G2 = [G[_].copy() for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            G2[i][j] = min(G2[i][j], G2[i][k] + G2[k][j])

            if G2[i][j] < G[i][j]:
                print(-1)
                exit()
ans = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if i == j: continue
        elif G2[i][j] == G[i][j]:
            v = G2[i][j]
            for k in range(N):
                if i == j or i == k or j == k: continue
                if G2[i][k] + G2[k][j] == G2[i][j]:
                    v = 0
                    break
            ans += v
print(ans)

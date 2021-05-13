def warshall_floyd(G, n):
    global c
    for i in range(n):
        for j in range(n):
            b = 1
            for k in range(n):
                if j == k or i == k:
                    continue
                if G[i][j] == G[i][k] + G[k][j]:
                    b = 0
                elif G[i][j] > G[i][k] + G[k][j]:
                    print(-1)
                    exit()
            if b == 1:
                c += G[i][j]

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
c = 0
warshall_floyd(a, n)
print(c // 2)
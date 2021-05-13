from itertools import permutations
N, W, R = map(int, input().split())
S = list(map(int, input().split()))

INFTY = 10**9
cost = [[INFTY]*(N+1) for _ in range(N+1)]

# 辺を入力
for _ in range(W):
    u, v, c = map(int, input().split())
    cost[u][v] = c
    cost[v][u] = c

# 自身に向かうコストは0
for i in range(N+1):
    cost[i][i] = 0


def WarshallFloyd():
    for k in range(N+1):
        for i in range(N+1):
            for j in range(N+1):
                cost[i][j] = min(cost[i][j], cost[i][k]+cost[k][j])


WarshallFloyd()

ans = 10**9
for T in permutations(S, R):
    temp = 0
    t = T[0]
    for i in range(1, R):
        temp += cost[t][T[i]]
        t = T[i]
    ans = min(ans, temp)
print(ans)

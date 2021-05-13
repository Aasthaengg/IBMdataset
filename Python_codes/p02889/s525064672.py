N, M, L = map(int, input().split())

INF = 10 ** 18
lst1 = [[INF] * (N + 1) for _ in range(N+1)] #頂点1に隣接する辺以外の道の管理
# u-->vへコストlで行ける時
for i in range(N+1):
    lst1[i][i] = 0
for _ in range(M):
    a, b, c = map(int, input().split())
    lst1[a][b] = c
    lst1[b][a] = c

# 処理する部分
def WarshallFloyd(lst):
    for k in range(N+1):
        for i in range(N+1):
            for j in range(N+1):
                lst[i][j] = min(lst[i][j], lst[i][k] + lst[k][j])
    return
# i-->jのコストはlst[i][j]

WarshallFloyd(lst1)

lst2 = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(N):
    lst2[i][i] = 0
    for j in range(i + 1, N + 1):
        if lst1[i][j] <= L:
            lst2[i][j] = 1
            lst2[j][i] = 1

WarshallFloyd(lst2)

Q = int(input())
for _ in range(Q):
    s, t = map(int, input().split())
    if lst2[s][t] >= INF:
        print (-1)
    else:
        print (max(lst2[s][t] - 1, 0))
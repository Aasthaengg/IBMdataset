N, M, Q = map(int, input().split())

# 入力
A = [[0 for j in range(N+1)] for i in range(N+1)]
for _ in range(M):
    L, R = map(int, input().split())
    A[L][R] += 1


# 二次元累積和
Cum = [[0 for j in range(N+1)] for i in range(N+1)]
for i in range(N):
    for j in range(N):
        Cum[i+1][j+1] = Cum[i][j+1] + Cum[i+1][j] - Cum[i][j] + A[i+1][j+1]

# クエリ処理
for _ in range(Q):
    p, q = map(int, input().split())
    print(Cum[q][q]-Cum[p-1][q]-Cum[q][p-1]+Cum[p-1][p-1])

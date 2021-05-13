# https://atcoder.jp/contests/agc032/tasks/agc032_b

# 補グラフ
N = int(input())
G = [[1 for _ in range(101)] for _ in range(101)]
for i in range(101): G[i][i] = 0
groups = []

if N % 2 == 1:
    for i in range(1, N // 2 + 1):
        # print(i, N - i)
        G[i][N - i] = G[N - i][i] = 0
    # print(N)
else:
    for i in range(1, N // 2 + 1):
        G[i][N - i + 1] = G[N - i + 1][i] = 0
        # print(i, N - i + 1)

M = 0
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        if G[i][j] == 1:
            M += 1
# for row in G[1:N+1]: print(*row[1:N+1])

print(M)
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        if G[i][j] == 1:
            print(i, j)

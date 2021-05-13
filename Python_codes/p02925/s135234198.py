N = int(input())

# 初期化
G = [[] for i in range(10 ** 6 + 1)]  # グラフ
U = [None] * (10 ** 6 + 1)  # 入次数
D = [0] * (10 ** 6 + 1)  # 根からの距離


# 変換用
def x(i, j):
    return j + 1000 * i


# グラフを構築
for i in range(1, N + 1):
    A = list(map(int, input().split()))
    for j in range(N - 2):
        fv1, fv2 = min(i, A[j]), max(i, A[j])
        tv1, tv2 = min(i, A[j + 1]), max(i, A[j + 1])
        G[x(fv1, fv2)].append(x(tv1, tv2))
        U[x(fv1, fv2)] = 0
        U[x(tv1, tv2)] = 0


# 入次数をカウント
for i in range(10 ** 6 + 1):
    for v in G[i]:
        U[v] += 1

# トポロジカルソート
U_zero_nodes = []
for i in range(10 ** 6 + 1):
    if U[i] is None:
        continue

    if U[i] == 0:
        U_zero_nodes.append(i)


topological_order = []
while U_zero_nodes:
    n = U_zero_nodes.pop()
    topological_order.append(n)

    for v in G[n]:
        U[v] -= 1
        if U[v] == 0:
            U_zero_nodes.append(v)


# 不可能判定
if len(topological_order) != N * (N - 1) // 2:
    print(-1)
    exit()


# 最長経路を計算
for t_n in topological_order:
    for v in G[t_n]:
        D[v] = max(D[v], D[t_n] + 1)
print(max(D) + 1)

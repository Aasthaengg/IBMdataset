from copy import deepcopy
# 多次元配列を作成する
def make_multi_list(initial, degree):
    ans = [initial for _ in range(degree[-1])]
    for d in reversed(degree[:-1]):
        ans = [deepcopy(ans) for _ in range(d)]
    return ans


N, C = map(int, input().split())
INF = float("inf")
D = []
for i in range(C):
    D.append(list(map(int, input().split())))
c = []
for i in range(N):
    c.append([n - 1 for n in list(map(int, input().split()))])

# 前計算
cost = make_multi_list(0, [3, C])
for i in range(N):
    for j in range(N):
        for k in range(C):
            cost[(i + j) % 3][k] += D[c[i][j]][k]

ans = INF
for i in range(C):
    for j in range(C):
        if i == j:
            continue
        for k in range(C):
            if k in (i, j):
                continue
            ans = min(ans, cost[0][i] + cost[1][j] + cost[2][k])

print(ans)

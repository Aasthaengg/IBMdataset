
def dfs_visit(u):
    global n, M, d, f, time

    if color[u] == 'WHITE':
        color[u] = 'GRAY'
        time += 1
        d[u] = time

        for v in range(n):
            if M[u][v] == 0:
                continue
            if color[v] == 'WHITE':
                dfs_visit(v)

        color[u] = 'BLACK'
        time += 1
        f[u] = time


def dfs():
    global n, M, d, f, time

    for u in range(n):
        if color[u] == 'WHITE':  # 連結グラフとは限らないため。
            dfs_visit(u)

    for u in range(n):
        print('{} {} {}'.format(u+1, d[u], f[u]))


n = int(input())

M = [[0 for i in range(n)] for j in range(n)]
color = ['WHITE'] * n  # 各頂点の色を記録。ホワイト（未探索）、グレイ（探索中）、ブラック（探索ずみ）
d = [None] * n  # vを最初に発見した時間
f = [None] * n  # vの完了時刻
time = 0

for i in range(n):
    _ = list(map(int, input().split()))
    u = _[0] - 1  # 0オリジンに変換

    degree = _[1]
    for j in range(degree):
        v = _[j+2] - 1  # 0オリジンに変換
        M[u][v] = 1

# for row in M:
#     print(' '.join(map(str, row)))

dfs()


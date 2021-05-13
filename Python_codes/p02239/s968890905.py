
def bfs(s):  # たぶんstartのs
    global n, M, color, d, q

    q.append(s)
    d[s] = 0

    while len(q) != 0:
        u = q.pop(0)

        for v in range(n):
            if M[u][v] != 1:
                continue

            if color[v] == 'WHITE':
                q.append(v)
                color[v] = 'GRAY'
                d[v] = d[u] + 1

        color[u] = 'BLACK'


n = int(input())

M = [[0 for i in range(n)] for j in range(n)]
color = ['WHITE'] * n  # 各頂点の色を記録。ホワイト（未探索）、グレイ（探索中）、ブラック（探索ずみ）
d = [-1] * n  # 始点0からvまでの距離
q = []

for i in range(n):
    _ = list(map(int, input().split()))
    u = _[0] - 1  # 0オリジンに変換

    degree = _[1]
    for j in range(degree):
        v = _[j+2] - 1  # 0オリジンに変換
        M[u][v] = 1

# for row in M:
#     print(' '.join(map(str, row)))

bfs(0)

for i in range(n):
    print('{} {}'.format(i+1, d[i]))


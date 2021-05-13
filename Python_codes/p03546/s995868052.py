# https://atcoder.jp/contests/abc079/tasks/abc079_d
# ワーシャルフロイド

h, w = map(int, input().split())
edge = [[] for _ in range(10)]
for i in range(10):
    edge[i] = list(map(int, input().split()))

num = [list(map(int, input().split())) for _ in range(h)]

for k in range(10):
    for i in range(10):
        for j in range(10):
            # iからjへの最短距離
            # 負の辺がある場合　つっこむとかなり遅くなる
            # if edge[i][k] != float('inf') and edge[k][j] != float('inf'):
            edge[i][j] = min(edge[i][j], edge[i][k] + edge[k][j])

ans = 0
for i in num:
    for j in i:
        if j == 1 or j == -1:
            continue
        else:
            ans += edge[j][1]

print(ans)

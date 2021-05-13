import itertools
N, M, R = map(int, input().split())
r_list = list(map(int, input().split()))

# iからjへの距離
# 町の番号は0-indexに直す
d = [[10**9 for _ in range(N)] for _ in range(N)]

# 0から0, ..., N-1からN-1への距離
for i in range(N):
    d[i][i] = 0

# aからbへの距離、bからaへの距離を記録
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    d[a][b] = c
    d[b][a] = c

# ワーシャルフロイド法
for k in range(N):  # 経由地点
    for i in range(N):  # スタート
        for j in range(N):  # ゴール
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

ans = 10**9

# 訪れる町の順列, 0-index
for p in itertools.permutations(r_list):
    tmp = 0
    for i in range(R - 1):
        x = p[i] - 1
        y = p[i + 1] - 1
        tmp += d[x][y]
    ans = min(ans, tmp)

print(ans)

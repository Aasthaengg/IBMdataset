H, W, K = map(int, input().split())
G = [list(input()) for i in range(H)]


# イチゴがない行の番号を記録しておく
non_placed_row_indexes = set()
for h in range(H):
    if G[h].count('#') == 0:
        non_placed_row_indexes.add(h)


ans = [[0] * W for i in range(H)]
painting = 0
for h in range(H):
    # イチゴがない行なら何もしない
    if h in non_placed_row_indexes:
        continue

    # 各行最初のイチゴは色を変えなくてよい（行の変化によって変わるので）
    find_flg = False
    for w in range(W):
        # 行が変わる
        if w == 0:
            painting += 1

        # イチゴを見つける
        if G[h][w] == '#':
            if find_flg:
                painting += 1
            else:
                find_flg = True

        ans[h][w] = painting


# １つ上の行を見ながら下にくだる
for h in range(1, H):
    # イチゴがある行なら何もしない
    if h not in non_placed_row_indexes:
        continue

    for w in range(W):
        # １つ上の行の色をコピー
        ans[h][w] = ans[h - 1][w]

# １つ下の行を見ながら上にのぼる
for h in range(H - 2, -1, -1):
    # イチゴがある行なら何もしない
    if h not in non_placed_row_indexes:
        continue

    for w in range(W):
        # １つ下の行の色をコピー
        ans[h][w] = ans[h + 1][w]


# 出力
for a in ans:
    print(*a, sep=' ')

# 白色マスで４方向のマスに黒マスが一つ以上存在するものを黒にかえる。
# 何回の操作でマスが全て黒マスになるか？
H, W = map(int, input().split())
field = [list(input()) for _ in range(H)]
black_list = []
for h in range(H):
    for w in range(W):
        if field[h][w] == "#":
            black_list.append((h, w))

count = 0
move = ((0, 1), (1, 0), (-1, 0), (0, -1))
# 広がり方は一点の黒から一定なのでそれを行うことで、計算量を改善できる？
while black_list:
    n_pl = []
    for b in black_list:
        for m in move:
            n_p = (b[0] + m[0], b[1] + m[1])
            if not(n_p[0] < 0 or n_p[1] < 0 or n_p[0] >= H or n_p[1] >= W) and field[n_p[0]][n_p[1]] == ".":
                field[n_p[0]][n_p[1]] = "#"
                n_pl.append(n_p)
    black_list = n_pl
    count += 1
print(count-1)

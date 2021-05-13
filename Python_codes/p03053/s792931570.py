H, W = map(int, input().rstrip().split())
checked = [[True]*(W+2)]
checked += [[True] + [ch == "#" for ch in input().rstrip()] + [True]
            for i in range(H)]
checked += [[True]*(W+2)]

black_list = []
# 初期化
# 0 => 黒、 -1 => 白
for i in range(1, H+1):
    for j in range(1, W+1):
        if checked[i][j]:
            black_list.append((i, j))

# 黒の周辺4方向のうち、白だったら黒にする
ans = -1
while black_list:
    ans += 1
    tmp = []
    for x, y in black_list:
        # 上
        if not checked[x-1][y]:
            checked[x-1][y] = True
            tmp.append((x-1, y))
        # 下
        if not checked[x+1][y]:
            checked[x+1][y] = True
            tmp.append((x+1, y))
        # 左
        if not checked[x][y-1]:
            checked[x][y-1] = True
            tmp.append((x, y-1))

        # 右
        if not checked[x][y+1]:
            checked[x][y+1] = True
            tmp.append((x, y+1))

    black_list = tmp

print(ans)

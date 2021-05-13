# https://atcoder.jp/contests/abc109/tasks/abc109_d

# 各マスにおいて、上下左右でいけるところに移動させる。
# と思ったけど、奇数同士が離れていた場合もあるな。
# ということで、まず奇数の枚数をカウントする。その割る2（繰り下げ）が
# 最大の枚数になる。
# その後は、コインが奇数枚のマスから、同じくコインが奇数枚のマスへの
# 最短経路を記録しておく。
# 一度選んだマスは、もう使えない。
# 提示された例に引きずられるとだめなやつだった。
# 一筆書きに、全部をなめるようにする。奇数だったら移動させて、偶数だったら無視する。
h, w = map(int, input().split())

matrix = []
for _ in range(h):
    matrix.append([int(i) for i in input().split()])


ans_move = []
for i in range(h):
    if i % 2 == 0: # 右に行く
        for j in range(w):
            if matrix[i][j] % 2 == 1:
                if j == w - 1 and i != h - 1: # 最右端
                    matrix[i][j] -= 1
                    matrix[i + 1][j] += 1
                    ans_move.append([i + 1, j + 1, i + 1 + 1, j + 1])
                elif j != w - 1:
                    matrix[i][j] -= 1
                    matrix[i][j + 1] += 1
                    ans_move.append([i + 1, j + 1, i + 1, j + 1 + 1])
    else: # 左に行く
        for j in range(w)[::-1]:
            if matrix[i][j] % 2 == 1:
                if j == 0 and i != h - 1: # 最左端
                    matrix[i][j] -= 1
                    matrix[i + 1][j] += 1
                    ans_move.append([i + 1, j + 1, i + 1 + 1, j + 1])
                elif j != 0:
                    matrix[i][j] -= 1
                    matrix[i][j - 1] += 1
                    ans_move.append([i + 1, j + 1, i + 1, j - 1 + 1])
ans = len(ans_move)
print(ans)
for m in ans_move:
    print(*m)

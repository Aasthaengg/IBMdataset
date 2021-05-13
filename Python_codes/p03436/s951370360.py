##いくつかの人の回答を参考に、メモしながら学習
H, W = map(int, input().split())
Field = [list(input()) for _ in range(H)]

# 10 37
# .....................................
# ...#...####...####..###...###...###..
# ..#.#..#...#.##....#...#.#...#.#...#.
# ..#.#..#...#.#.....#...#.#...#.#...#.
# .#...#.#..##.#.....#...#.#.###.#.###.
# .#####.####..#.....#...#..##....##...
# .#...#.#...#.#.....#...#.#...#.#...#.
# .#...#.#...#.##....#...#.#...#.#...#.
# .#...#.####...####..###...###...###..
# .....................................

# 出力するスコアは「全白マス数」-「最短距離のマス数」なので、まず白マスの数を数える。
white = 0
for i in range(H):
    for j in range(W):
        if Field[i][j] == '.':
            white += 1

# 移動する4方向
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# HxWの行列を作る。初期値は全部"None"。ここにスタートからゴールまでの歩数を入れていく。
    # Field_map[H-1][W-1]がゴールまでの「最短距離のマス数」になる。
Field_cost =[[None]*W for i in range(H)]
Field_cost[0][0] = 0

# whileでゴールまでの最短距離を幅優先探索
from collections import deque
que = deque([])     # デックリストqueに、最短距離を通る際の(i,j)が入っていく。
que.append((0, 0))  # まず(0,0)は通るので。

while que:
    i, j = que.popleft()       # (i,j)が今いるマス
    if i == H-1 and j == W-1:  # (i,j)がゴールマスになったらやめ
        break
    for d in range(4):
        new_i = i + dx[d]
        new_j = j + dy[d]
        if 0 <= new_i and new_i < H and \
           0 <= new_j and new_j < W and \
           Field[new_i][new_j] != '#' and \
           Field_cost[new_i][new_j] == None:  # 1,2は道を外れてないこと。3はちゃんと白マス。4はまだ通ってないこと。
            que.append((new_i, new_j))     # このマス
            Field_cost[new_i][new_j] = Field_cost[i][j] + 1  # 前のマス+1。何マス歩いてきたか。

# 出力するスコアは「全白マス数」-「最短距離のマス数」
if Field_cost[H-1][W-1] is None:
    print("-1")
else:
    print(white - Field_cost[H-1][W-1]-1)

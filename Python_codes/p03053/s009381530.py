# https://atcoder.jp/contests/agc033/tasks/agc033_a

from collections import deque
import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]     # 動ける場所の候補


def debug(start, goal, p, t):
    player = p
    debug_grid = list(list(grid[h]) for h in range(H))
    if start != (None, None):
        debug_grid[start[0]][start[1]] = "S"
    if goal != (None, None):
        debug_grid[goal[0]][goal[1]] = "G"
    debug_grid[player[0]][player[1]] = "P"
    print("~~~~~~~~~ t = " + str(t+1) + "  ~~~~~~~~")
    for debug_h in range(H):
        print("".join(str(debug_grid[debug_h][debug_w]) for debug_w in range(W)))


def search(grid, next_set, goal=(None,None), visit=set()):
    visit.add(start)                            # スタート地点はすでに訪れている
    while next_set:                             # p = [] になったら止める
        p, t = next_set.popleft()               # 要素を消去して、消去した要素を出力
        h, w = p
        for dh, dw in move:                     # 頂点 p から進める経路の候補から一つ選ぶ
            q = (h + dh, w + dw)
            if q[0] < 0 or q[0] >= H or q[1] < 0 or q[1] >= W:
                continue
            if grid[q[0]][q[1]] == wall:         # 壁があったら進まない
                continue
            if q in visit:                      # 一度訪れていた場合は進まない
                continue
            #### (debug code) ######
            # debug(start, goal, q, t)
            ########################
            if q == goal:                       # ゴールがあるならば、ここで判定
                return t + 1                    # 経路の長さは t + 1 で与えられる
            visit.add(q)                        # 頂点 q に一度訪れた事をメモ (for の前に書くと、ここで選ばれた q が最短であるはずなのに、違う経路でvisit = Trueを踏んでしまう可能性がある)
            next_set.append((q, t + 1))         # p から q へと移動。時刻を 1 進める
    return t



road, wall = ".", "#"                         # (進行可能を意味する記号, 進行不可を意味する記号)

H,W = map(int,input().split())                # 左上は(h,w)=(0,0)、右下は(h,w)=(H-1,W-1)

grid = []
next_set = deque()
visit = set()
for h in range(H):
    grid.append(input())
    for w, a in enumerate(grid[-1]):
        if a == "#":
            start = (h, w)
            next_set.append((start,0))
            visit.add(start)

print(search(grid, next_set, goal=(None,None), visit=visit))
import sys
input = sys.stdin.readline
from collections import deque

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]     # 動ける場所の候補

def debug(p, t):
    player = p
    debug_grid = list(list(grid[h]) for h in range(H))
    debug_grid[start[0]][start[1]] = "S"
    debug_grid[goal[0]][goal[1]] = "G"
    debug_grid[player[0]][player[1]] = "P"
    print("~~~~~~~~~ t = " + str(t+1) + "  ~~~~~~~~")
    for debug_h in range(H):
        print("".join(debug_grid[debug_h][debug_w] for debug_w in range(W)))

def search(start=(0,0), goal=(None,None), visit=set()):
    visit.add(start)                            # スタート地点はすでに訪れている
    next_set = deque([(start, 0)])              # 次に進む候補を列挙する。スタック（右から取り出す = pop）だと深さ優先になり、キュー（左から取り出す = popleft）だと幅優先になる
                                                # 第一成分はスタート地点、第二成分は時刻を表す。
    while next_set:                             # p = [] になったら止める
        p, t = next_set.popleft()               # 要素を消去して、消去した要素を出力
        h, w = p
        for dh, dw in move:                     # 頂点 p から進める経路の候補から一つ選ぶ
            q = (h + dh, w + dw)
            if q[0] < 0 or q[0] >= H or q[1] < 0 or q[1] >= W:
                continue
            if grid[q[0]][q[1]] == "#":         # 壁があったら進まない
                continue
            if q in visit:                      # 一度訪れていた場合は進まない
                continue
            #### (debug code) ######
            # debug(q, t)
            ########################
            if q == goal:                       # ゴールがあるならば、ここで判定
                return t + 1                    # 経路の長さは t + 1 で与えられる
            visit.add(q)                        # 頂点 q に一度訪れた事をメモ (for の前に書くと、ここで選ばれた q が最短であるはずなのに、違う経路でvisit = Trueを踏んでしまう可能性がある)
            next_set.append((q, t + 1))         # p から q へと移動。時刻を 1 進める
    return -1


H,W = map(int,input().split())                # 左上は(h,w)=(0,0)、右下は(h,w)=(H-1,W-1)

grid = []
cnt = 0

for h in range(H):
    grid.append(input())
    cnt += grid[-1].count(".")
start = (0,0)
goal = (H-1, W-1)
res = search(start,goal)
if res == -1:
    print(-1)
else:
    print(cnt - res - 1)
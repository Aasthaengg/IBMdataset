from collections import deque

h, w = map(int, input().split())

S = [[] for _ in range(h)]
# まず、最初にある白マスの数を数えておく
ans = 0
for i in range(h):
    S[i] = input()
    ans += S[i].count('.')

direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]

# BFS
# 距離を初期化.
D = [[-1] * w for _ in range(h)]
D[0][0] = 0

# 現在地でキューを初期化.
que = deque([[0, 0]])

# キューがなくなるまで探索を行う.
while que:
    # キュー（右から）を一つ取り出す.
    chi, cwi = que.pop()

    for (dh, dw) in direct:
        # 迷路の範囲外なら探索しない.
        if not (0 <= chi + dh <= h - 1 and 0 <= cwi + dw <= w - 1):
            continue
        # 探索済みや探索不可なところは探索しない.
        if D[chi + dh][cwi + dw] != -1 or S[chi + dh][cwi + dw] == '#':
            continue
        # 距離の計算.
        D[chi + dh][cwi + dw] = D[chi][cwi] + 1
        # 次に探索する場所の追加.
        que.appendleft([chi + dh, cwi + dw])

dist = D[-1][-1]
# もともとあった白マスの数 - (ゴールまでに辿る最小の白マス+スタートの1マス)
if dist != -1:
    print(ans - (dist + 1))
else:
    print(-1)

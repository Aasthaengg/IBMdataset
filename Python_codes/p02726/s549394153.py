from collections import deque

N, X, Y = [int(x) for x in input().split()]
result = {x: 0 for x in range(N)}

# 面倒なので0オリジンに修正
X -= 1
Y -= 1

# 全位置から移動できるパターンを幅優先探索で網羅する
for i in range(N):

    queue = deque()
    visited = set()

    # 開始位置と距離を初期値として入れる
    queue.appendleft((i, 0))

    while queue:
        now_pos, distance = queue.pop()

        # 訪れていない場合、その位置に移動するまでの距離に結果を加算
        # 訪問済フラグを立てる
        if not now_pos in visited:
            result[distance] += 1
            visited.add(now_pos)

        # 前、後ろ、X <-> Y の移動を実行
        # すでに訪問済の場合は追加しない
        if now_pos - 1 >= 0:
            if not now_pos - 1 in visited:
                queue.appendleft((now_pos - 1, distance + 1))

        if now_pos + 1 < N:
            if not now_pos + 1 in visited:
                queue.appendleft((now_pos + 1, distance + 1))

        if now_pos == X:
            if not Y in visited:
                queue.appendleft((Y, distance+1))

        if now_pos == Y:
            if not X in visited:
                queue.appendleft((X, distance+1))

for i in range(1, N):
    print(result[i] // 2)

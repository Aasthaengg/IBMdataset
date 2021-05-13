from collections import deque


def bfs(S):  # 幅優先探索  # キュー
    dist = [[-1] * w for _ in range(h)]  # 前処理
    que = deque()
    for i, Si in enumerate(S):
        for j, Sij in enumerate(Si):
            if Sij == '#':
                dist[i][j] = 0
                que.append((i, j))

    while len(que) > 0:
        (x, y) = que.popleft()
        near = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        for i, j in near:  # 移動先の候補
            if 0 <= i < h and 0 <= j < w and dist[i][j] < 0:
                dist[i][j] = dist[x][y] + 1
                que.append((i, j))
    return max(max(ans) for ans in dist)


h, w = map(int, input().split())
a = [input() for _ in range(h)]
print(bfs(a))

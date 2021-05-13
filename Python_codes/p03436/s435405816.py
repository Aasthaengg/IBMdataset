from collections import deque


def main():
    H, W = map(int, input().rstrip().rsplit())

    visited = [[0]*(W+2) for i in range(H+2)]
    maze = [["#"]*(W+2)]

    black_cnt = 0
    for i in range(H):
        # 黒色のマス目の数をカウント
        row = input().rstrip()
        black_cnt += row.count("#")

        # maze作成
        row = "#" + row + "#"
        maze.append(list(row))

    maze.append(["#"]*(W+2))

    # 幅優先探索で始点からの距離を求める
    queue = deque([(1, 1)])

    while queue:
        x, y = queue.popleft()
        # 黒マスの時
        if maze[x][y] == "#":
            continue

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            # 探索済みかチェック
            if visited[x+dx][y+dy] > 0:
                continue
            # 次のマス目候補に経路長を入れる
            visited[x+dx][y+dy] = visited[x][y] + 1

            # 探索候補に追加
            queue.append((x+dx, y+dy))

    if visited[H][W] == 0:
        print(-1)
        return
    ans = H*W - black_cnt - visited[H][W] - 1
    print(ans)


if __name__ == "__main__":
    main()
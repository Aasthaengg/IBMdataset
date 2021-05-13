h, w = map(int, input().split())
board = []

for _ in range(h):
    board.append(input())

dx = [0, 0, 1, 1, 1, -1, -1, -1]
dy = [1, -1, -1, 0, 1, -1, 0, 1]

for i in range(h):
    for j in range(w):
        if board[i][j] == "#":
            continue
        cnt = 0

        for d in range(8):
            ni = i + dy[d]
            nj = j + dx[d]

            if (ni < 0 or ni >= h) or (nj < 0 or nj >= w):
                continue
            if board[ni][nj] == "#":
                cnt += 1

        temp_board = list(board[i])
        temp_board[j] = str(cnt)
        board[i] = "".join(temp_board)

for i in range(h):
    print(board[i])
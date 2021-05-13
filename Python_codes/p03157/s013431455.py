H, W = map(int, input().split())

S = [list(input()) for _ in range(H)]

check = [[0] * W for _ in range(H)]

ans = 0

move = [[1, 0], [-1, 0], [0, 1], [0, -1]]

for h in range(H):
    for w in range(W):
        if check[h][w] == 1:
            continue
        black = 0
        white = 0

        stack = [[h, w]]
        check[h][w] = 1
        if S[h][w] == '#':
            black += 1
        elif S[h][w] == '.':
            white += 1

        while len(stack) != 0:
            x, y = stack.pop()
            tmp = S[x][y]
            for dx, dy in move:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < H and 0 <= ny < W and tmp != S[nx][ny] and check[nx][ny] == 0:
                    check[nx][ny] = 1
                    stack.append([nx, ny])
                    if S[nx][ny] == '#':
                        black += 1
                    elif S[nx][ny] == '.':
                        white += 1
        
        ans += black * white

print (ans)
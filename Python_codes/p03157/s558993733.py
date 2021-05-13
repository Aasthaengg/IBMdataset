# aising2019C - Alternating Path
def dfs(sx: int, sy: int) -> None:
    color, stack = [0] * 2, [(sx, sy, S[sx][sy])]
    S[sx][sy] = 2  # make the grid visited
    while stack:
        x, y, col = stack.pop()
        color[col] += 1
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and S[nx][ny] == col ^ 1:
                stack.append((nx, ny, S[nx][ny]))
                S[nx][ny] = 2  # make the grid visited
    return color[0] * color[1]


def main():
    # separate S to connected components
    global H, W, S, dxy
    H, W, *S = open(0).read().split()
    H, W = int(H), int(W)
    S = [[1 if i == "#" else 0 for i in s] for s in S]
    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] != 2:
                ans += dfs(i, j)
    print(ans)


if __name__ == "__main__":
    main()
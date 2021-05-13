# aising2019C - Alternating Path
import sys

sys.setrecursionlimit(10 ** 9)


def dfs(x: int, y: int) -> None:
    global blk, wht
    cur = S[x][y]
    S[x][y] = 2  # make the grid visited
    if cur:
        blk += 1
    else:
        wht += 1
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if 0 <= nx < H and 0 <= ny < W and S[nx][ny] == cur ^ 1:
            dfs(nx, ny)


def main():
    # separate S to connected components
    global H, W, S, dxy, blk, wht
    H, W, *S = open(0).read().split()
    H, W = int(H), int(W)
    S = [[1 if i == "#" else 0 for i in s] for s in S]
    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] != 2:
                blk, wht = 0, 0
                dfs(i, j)
                ans += blk * wht
    print(ans)


if __name__ == "__main__":
    main()
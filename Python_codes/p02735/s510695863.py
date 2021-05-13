import sys

sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    H, W = map(int, input().split())
    maze = [[_ for _ in input()] for _ in range(W)]
    INF = 10 ** 5
    
    # dp[i][j]:=(i,j)に到達するまでに黒壁を壊す回数の最小値
    dp = [[INF] * W for _ in range(H)]
    
    if maze[0][0] == '#':
        dp[0][0] = 1
    else:
        dp[0][0] = 0
    
    for i in range(H):
        for j in range(W):
            for [dy, dx] in [[1, 0], [0, 1]]:
                ny, nx = i + dy, j + dx
                if ny >= H or nx >= W:
                    continue
                else:
                    if maze[i][j] == '.' and maze[ny][nx] == '#':
                        dp[ny][nx] = min(dp[ny][nx], dp[i][j] + 1)
                    else:
                        dp[ny][nx] = min(dp[ny][nx], dp[i][j])
    print(dp[H - 1][W - 1])


resolve()
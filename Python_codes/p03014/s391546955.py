import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    grid = [list(input().rstrip()) for _ in range(H)]

    cnt_w = [[0] * W for _ in range(H)]
    for h in range(H):
        cnt = 0
        for w in range(W):
            if grid[h][w] == "#":
                cnt = 0
            else:
                cnt += 1
            cnt_w[h][w] = cnt

    for h in range(H):
        cnt = 0
        for w in reversed(range(W)):
            if grid[h][w] == "#":
                cnt = 0
            else:
                cnt = max(cnt, cnt_w[h][w])
            cnt_w[h][w] = cnt

    cnt_h = [[0] * W for _ in range(H)]
    for w in range(W):
        cnt = 0
        for h in range(H):
            if grid[h][w] == "#":
                cnt = 0
            else:
                cnt += 1
            cnt_h[h][w] = cnt

    for w in range(W):
        cnt = 0
        for h in reversed(range(H)):
            if grid[h][w] == "#":
                cnt = 0
            else:
                cnt = max(cnt, cnt_h[h][w])
            cnt_h[h][w] = cnt

    res = 0
    for h in range(H):
        for w in range(W):
            res = max(res, cnt_w[h][w] + cnt_h[h][w] - 1)
    print(res)


if __name__ == '__main__':
    resolve()

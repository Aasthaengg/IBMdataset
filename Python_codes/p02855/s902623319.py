import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    H, W, K = map(int, input().split())
    S = [input() for _ in range(H)]

    ans = [[None] * W for _ in range(H)]

    cnt = 1
    for h in range(H):
        for w in range(W):
            if S[h][w] == "#":
                ans[h][w] = cnt
                cnt += 1

    # 上から下
    for h in range(1, H):
        for w in range(W):
            if ans[h][w] is None:
                if ans[h - 1][w] is not None:
                    ans[h][w] = ans[h - 1][w]

    # 下から上
    for h in range(H - 1)[::-1]:
        for w in range(W):
            if ans[h][w] is None:
                if ans[h + 1][w] is not None:
                    ans[h][w] = ans[h + 1][w]

    # 左から右
    for h in range(H):
        for w in range(1, W):
            if ans[h][w] is None:
                if ans[h][w - 1] is not None:
                    ans[h][w] = ans[h][w - 1]

    # 右から左
    for h in range(H):
        for w in range(W - 1)[::-1]:
            if ans[h][w] is None:
                if ans[h][w + 1] is not None:
                    ans[h][w] = ans[h][w + 1]

    for h in range(H):
        print(*ans[h], sep=" ")


if __name__ == "__main__":
    main()

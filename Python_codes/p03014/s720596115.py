import sys
import math  # noqa
import bisect  # noqa
import queue  # noqa


def input():
    return sys.stdin.readline().rstrip()


def main():
    H, W = map(int, input().split())
    S = [[s for s in input()] for _ in range(H)]

    hori = [[0 for _ in range(W)] for _ in range(H)]
    for i in range(H):
        cnt = 0
        for j in range(W):
            if S[i][j] == '.':
                cnt += 1
                hori[i][j] = cnt
            else:
                cnt = 0
        res = 0
        for j in range(W - 1, -1, -1):
            if S[i][j] == '.':
                res = max(res, hori[i][j])
                hori[i][j] = res
            else:
                res = 0

    vert = [[0 for _ in range(W)] for _ in range(H)]
    for i in range(W):
        cnt = 0
        for j in range(H):
            if S[j][i] == '.':
                cnt += 1
                vert[j][i] = cnt
            else:
                cnt = 0
        res = 0
        for j in range(H - 1, -1, -1):
            if S[j][i] == '.':
                res = max(res, vert[j][i])
                vert[j][i] = res
            else:
                res = 0

    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                ans = max(ans, hori[i][j] + vert[i][j] - 1)

    print(ans)


if __name__ == '__main__':
    main()

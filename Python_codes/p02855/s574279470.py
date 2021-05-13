import sys
import math  # noqa
import bisect  # noqa
import queue  # noqa


def input():
    return sys.stdin.readline().rstrip()


if __name__ == '__main__':
    H, W, K = map(int, input().split())
    S = [[s for s in input()] for _ in range(H)]

    ans = [[0 for _ in range(W)] for _ in range(H)]
    cnt = 1
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                ans[i][j] = cnt
                cnt += 1

    for i in range(H):
        res = 0
        for j in range(W):
            if ans[i][j] == 0:
                ans[i][j] = res
            else:
                res = ans[i][j]
        res = 0
        for j in range(W - 1, -1, -1):
            if ans[i][j] == 0:
                ans[i][j] = res
            else:
                res = ans[i][j]

    for i in range(W):
        res = 0
        for j in range(H):
            if ans[j][i] == 0:
                ans[j][i] = res
            else:
                res = ans[j][i]
        res = 0
        for j in range(H - 1, -1, -1):
            if ans[j][i] == 0:
                ans[j][i] = res
            else:
                res = ans[j][i]

    for a in ans:
        print(*a)

import sys
import math  # noqa
import bisect  # noqa
import queue  # noqa


def input():
    return sys.stdin.readline().rstrip()


def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    N = 0
    res = []
    for h in range(H):
        for w in range(W):
            if A[h][w] == 0:
                continue
            d = ((-1, 0), (0, -1))
            flag = False
            for dh, dw in d:
                nh = h + dh
                nw = w + dw
                if nh < 0 or H <= nh or nw < 0 or W <= nw:
                    continue
                if A[nh][nw] % 2 != 0:
                    N += 1
                    res.append((h + 1, w + 1, nh + 1, nw + 1))
                    A[h][w] -= 1
                    A[nh][nw] += 1
                    flag = True
                    break
            if flag:
                continue
            d = ((0, 1), (1, 0))
            for dh, dw in d:
                nh = h + dh
                nw = w + dw
                if nh < 0 or H <= nh or nw < 0 or W <= nw:
                    continue
                if A[h][w] % 2 != 0:
                    N += 1
                    res.append((h + 1, w + 1, nh + 1, nw + 1))
                    A[h][w] -= 1
                    A[nh][nw] += 1
                    break

    print(N)
    for r in res:
        print(*r)


if __name__ == '__main__':
    main()

import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    X, Y = [], []
    XY = []
    for _ in range(n):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
        XY.append([x, y])
    X.sort()
    Y.sort()

    res = f_inf
    for x1 in range(n):
        left = X[x1]
        for x2 in range(x1 + 1, n):
            right = X[x2]
            for y1 in range(n):
                bottom = Y[y1]
                for y2 in range(y1 + 1, n):
                    up = Y[y2]
                    cnt = 0
                    for x, y in XY:
                        if left <= x <= right and bottom <= y <= up:
                            cnt += 1
                        if cnt >= k:
                            area = (right - left) * (up - bottom)
                            res = min(res, area)
                            break
    print(res)


if __name__ == '__main__':
    resolve()

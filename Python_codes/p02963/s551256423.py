import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')


def resolve():
    s = int(input())
    x0, y0 = 0, 0
    if s % (10 ** 9) == 0:
        x1, y1 = 10 ** 9, 0
    else:
        x1, y1 = 10 ** 9, 1

    y2 = (s + x1 - 1) // x1
    x2 = 10 ** 9 - s % x1
    print(x0, y0, x1, y1, x2, y2)
    # print(s - abs(x1 * y2 - x2 * y1))


if __name__ == '__main__':
    resolve()

import sys
from itertools import accumulate

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    W, H, N, *XYA = map(int, read().split())

    x_left = 0
    x_right = W
    y_left = 0
    y_right = H
    for x, y, a in zip(*[iter(XYA)] * 3):
        if a == 1 and x_left < x:
            x_left = x
        elif a == 2 and x_right > x:
            x_right = x
        elif a == 3 and y_left < y:
            y_left = y
        elif a == 4 and y_right > y:
            y_right = y

    print(max(x_right - x_left, 0) * max(y_right - y_left, 0))
    return


if __name__ == '__main__':
    main()

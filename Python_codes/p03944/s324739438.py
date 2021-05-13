import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    w, h, n = map(int, readline().split())

    x_max = w
    x_min = 0
    y_max = h
    y_min = 0

    for _ in range(n):
        x, y, a = map(int, readline().split())
        if a == 1:
            x_min = max(x_min, x)
        elif a == 2:
            x_max = min(x_max, x)
        elif a == 3:
            y_min = max(y_min, y)
        else:
            y_max = min(y_max, y)

    print(max(0, (x_max - x_min)) * max(0, (y_max - y_min)))


if __name__ == '__main__':
    main()

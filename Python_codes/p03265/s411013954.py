import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    x1, y1, x2, y2 = map(int, readline().split())
    p = x2 - x1
    q = y2 - y1

    x3 = x2 - q
    y3 = y2 + p
    x4 = x1 - q
    y4 = y1 + p

    print(x3, y3, x4, y4)


if __name__ == '__main__':
    main()

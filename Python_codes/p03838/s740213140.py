import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    x, y = map(int, input().split())
    if x == 0:
        if y >= 0:
            print(y - x)
        else:
            print(-y + 1)
    elif y == 0:
        if x >= 0:
            print(x + 1)
        else:
            print(-x)
    elif 0 < x < y:
        print(y - x)
    elif 0 < y < x:
        print(2 + x - y)
    elif x < y < 0:
        print(y - x)
    elif y < x < 0:
        print(x - y + 2)
    elif x < 0 < y:
        print(abs(abs(x) - abs(y)) + 1)
    else:
        print(abs(abs(x) - abs(y)) + 1)


if __name__ == "__main__":
    main()

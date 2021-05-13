import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    x, y = map(int, readline().split())
    ans = 0
    if x < y:
        if x >= 0:
            ans = y - x
        elif y >= 0:
            ans = min(y - x, abs(y - abs(x)) + 1)
        else:
            ans = y - x
    else:
        if y >= 0:
            ans = min(x - y + 2, x + y + 1)
        elif x >= 0:
            ans = abs(x - abs(y)) + 1
        else:
            ans = abs(y) - abs(x) + 2

    print(ans)


if __name__ == '__main__':
    main()

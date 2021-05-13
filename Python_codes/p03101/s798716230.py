import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    h, w = map(int, readline().split())
    p, q = map(int, readline().split())

    print(h * w - p * w - q * (h - p))


if __name__ == '__main__':
    main()

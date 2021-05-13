import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    x, a, b = map(int, readline().split())

    if b <= a:
        print("delicious")
    elif b - a <= x:
        print("safe")
    else:
        print("dangerous")


if __name__ == '__main__':
    main()

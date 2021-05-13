import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    K = int(readline())

    x = K // 2
    y = (K + 1) // 2

    print(x * y)


if __name__ == '__main__':
    main()

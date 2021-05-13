import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    X = list(map(int, readline().split()))

    print(max(X) - min(X))


if __name__ == '__main__':
    main()

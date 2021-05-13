import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N, A, B = map(int, readline().split())

    print(min(N * A, B))


if __name__ == '__main__':
    main()

import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    K, X = map(int, readline().split())
    res = [x for x in range(X - K + 1, X + K)]
    print(*res)


if __name__ == '__main__':
    main()

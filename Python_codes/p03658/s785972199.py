import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N, K = map(int, readline().split())
    l = list(map(int, readline().split()))

    l.sort(reverse=True)

    print(sum(l[:K]))


if __name__ == '__main__':
    main()

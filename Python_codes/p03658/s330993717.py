import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, K, *L = map(int, read().split())

    L.sort(reverse=True)

    print(sum(L[:K]))

    return


if __name__ == '__main__':
    main()

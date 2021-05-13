import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *P = map(int, read().split())

    k = sum(1 for i, p in enumerate(P, 1) if i != p)

    if k > 2:
        print('NO')
    else:
        print('YES')


if __name__ == '__main__':
    main()

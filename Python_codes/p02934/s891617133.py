import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *A = map(int, read().split())

    p = 1
    for a in A:
        p *= a

    denom = 0
    for a in A:
        denom += p // a

    print(p / denom)
    return


if __name__ == '__main__':
    main()

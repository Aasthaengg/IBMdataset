import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *A = map(int, read().split())

    neg = sum(1 for a in A if a < 0)
    ans = sum(abs(a) for a in A)

    if neg % 2 == 1:
        ans -= 2 * min(abs(a) for a in A)

    print(ans)
    return


if __name__ == '__main__':
    main()

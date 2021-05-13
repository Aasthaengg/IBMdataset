import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *A = map(int, read().split())

    d = dict()
    for a in A:
        if a in d and d[a]:
            d[a] = False
        else:
            d[a] = True

    ans = sum(1 for flag in d.values() if flag)

    print(ans)
    return


if __name__ == '__main__':
    main()

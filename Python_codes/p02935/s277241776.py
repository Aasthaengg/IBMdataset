import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *V = map(int, read().split())

    V.sort()
    ans = V[0]
    for v in V[1:]:
        ans = (ans + v) / 2

    print(ans)
    return


if __name__ == '__main__':
    main()

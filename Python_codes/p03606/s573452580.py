import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *LR = map(int, read().split())

    ans = 0
    for l, r in zip(*[iter(LR)] * 2):
        ans += r - l + 1

    print(ans)
    return


if __name__ == '__main__':
    main()

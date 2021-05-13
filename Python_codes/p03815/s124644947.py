import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    x = int(readline())

    ans = x // 11 * 2
    x %= 11
    if 0 < x <= 6:
        ans += 1
    elif x > 6:
        ans += 2

    print(ans)
    return


if __name__ == '__main__':
    main()

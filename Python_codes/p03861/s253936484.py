import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    a, b, x = map(int, readline().split())

    if b == 0:
        ans = 1
    elif a == 0:
        ans = b // x + 1
    else:
        ans = b // x - (a - 1) // x

    print(ans)
    return


if __name__ == '__main__':
    main()

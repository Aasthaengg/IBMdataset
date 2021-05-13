import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    X, Y = map(int, readline().split())

    a = X
    ans = 1
    while X * 2 <= Y:
        X *= 2
        ans += 1

    print(ans)
    return


if __name__ == '__main__':
    main()

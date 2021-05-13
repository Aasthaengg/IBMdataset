import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    D, N = map(int, readline().split())

    ans = pow(100, D)
    if N < 100:
        ans *= N
    else:
        ans *= 101

    print(ans)

    return


if __name__ == '__main__':
    main()

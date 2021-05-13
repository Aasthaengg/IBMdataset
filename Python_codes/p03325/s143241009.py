import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *A = map(int, read().split())

    ans = 0
    for a in A:
        while a % 2 == 0:
            ans += 1
            a //= 2

    print(ans)
    return


if __name__ == '__main__':
    main()

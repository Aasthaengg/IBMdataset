import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    A = list(map(int, readline().split()))

    Asum = sum(A)
    Amax = max(A)

    if Asum % 2 == 3 * Amax % 2:
        ans = (3 * Amax - Asum) // 2
    else:
        ans = (3 * (Amax + 1) - Asum) // 2

    print(ans)
    return


if __name__ == '__main__':
    main()

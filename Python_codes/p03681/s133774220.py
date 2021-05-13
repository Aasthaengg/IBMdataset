import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, M = map(int, read().split())

    if abs(N - M) > 1:
        print(0)
        return

    COM_MAX = max(N, M)

    fac = [0] * (COM_MAX + 1)
    fac[0] = fac[1] = 1
    for i in range(2, COM_MAX + 1):
        fac[i] = fac[i - 1] * i % MOD

    if N == M:
        ans = 2 * fac[N] * fac[M] % MOD
    else:
        ans = fac[N] * fac[M] % MOD

    print(ans)
    return


if __name__ == '__main__':
    main()

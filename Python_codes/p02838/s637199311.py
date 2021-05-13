import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *A = map(int, read().split())
    M = 61
    for i, a in enumerate(A):
        A[i] = list(map(int, str(format(a, 'b')).zfill(M)[::-1]))

    csum = [[0] * M for _ in range(N)]
    csum[0] = A[0]
    for i in range(1, N):
        for j in range(M):
            csum[i][j] = csum[i - 1][j] + A[i][j]

    p2 = [0] * M
    p2[0] = 1
    for i in range(M - 1):
        p2[i + 1] = p2[i] * 2 % MOD

    B = [0] * M
    for i, a in enumerate(A[1:], 1):
        for j in range(M):
            B[j] += csum[i - 1][j] if a[j] == 0 else i - csum[i - 1][j]

    ans = 0
    for j in range(M):
        ans = (ans + B[j] * p2[j]) % MOD

    print(ans)
    return


if __name__ == '__main__':
    main()

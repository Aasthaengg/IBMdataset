import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    H, W, D = map(int, readline().split())
    A = [list(map(int, readline().split())) for _ in range(H)]
    Q, *LR = map(int, read().split())

    vec = [0] * (H * W + 1)
    for i in range(H):
        for j in range(W):
            vec[A[i][j]] = (i + 1, j + 1)
    vec[0] = vec[D]

    csum = [0] * D
    for i in range(D):
        N = (H * W - i) // D + 1
        csum[i] = [0] * N
        for j in range(N - 1):
            csum[i][j + 1] = (
                csum[i][j]
                + abs(vec[i + (j + 1) * D][0] - vec[i + j * D][0])
                + abs(vec[i + (j + 1) * D][1] - vec[i + j * D][1])
            )

    ans = [0] * Q
    for i, (l, r) in enumerate(zip(*[iter(LR)] * 2)):
        n, m = divmod(l, D)
        ans[i] = csum[m][(r - l) // D + n] - csum[m][n]

    print('\n'.join(map(str, ans)))
    return


if __name__ == '__main__':
    main()

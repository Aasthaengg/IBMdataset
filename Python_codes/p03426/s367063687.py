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

    csum = [0] * (H * W + 1)
    for i in range(D + 1, H * W + 1):
        csum[i] = csum[i - D] + abs(vec[i][0] - vec[i - D][0]) + abs(vec[i][1] - vec[i - D][1])

    ans = [0] * Q
    for i, (l, r) in enumerate(zip(*[iter(LR)] * 2)):
        ans[i] = csum[r] - csum[l]

    print('\n'.join(map(str, ans)))
    return


if __name__ == '__main__':
    main()

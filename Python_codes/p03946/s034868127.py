import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, T, *A = map(int, read().split())

    B = [0] * N
    B[0] = INF
    for i in range(N - 1):
        if B[i] > A[i]:
            B[i + 1] = A[i]
        else:
            B[i + 1] = B[i]

    p = 0
    C = [0] * N
    for i in range(N):
        C[i] = A[i] - B[i]
        if p < C[i]:
            p = C[i]

    ans = C.count(p)

    print(ans)
    return


if __name__ == '__main__':
    main()

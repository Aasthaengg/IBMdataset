import sys

read = sys.stdin.buffer.read


def main():
    N, M, Q, *LRPQ = map(int, read().split())
    LR = LRPQ[: 2 * M]
    PQ = LRPQ[2 * M :]
    
    A = [[0] * (N + 1) for _ in range(N + 1)]
    for l, r in zip(LR[::2], LR[1::2]):
        A[l][r] += 1

    for i in range(N):
        for j in range(N):
            A[i + 1][j + 1] += A[i][j + 1] + A[i + 1][j] - A[i][j]

    ans = [0] * Q
    for i, (p, q) in enumerate(zip(PQ[::2], PQ[1::2])):
        ans[i] = A[q][q] - A[q][p - 1] - A[p - 1][q] + A[p - 1][p - 1]

    print('\n'.join(map(str, ans)))
    return


if __name__ == '__main__':
    main()

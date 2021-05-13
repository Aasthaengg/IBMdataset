import sys

readline = sys.stdin.readline


def main():
    S = readline().strip()
    N = len(S)
    M = 10 ** 5
    K = len(bin(M)) - 2

    A = [[0] * N for _ in range(K)]
    for i, c in enumerate(S):
        if c == 'R':
            A[0][i] += i + 1
        else:
            A[0][i] += i - 1

    for k in range(K - 1):
        for i in range(N):
            A[k + 1][i] = A[k][A[k][i]]

    B = list(range(N))
    ans = [0] * N
    for k in range(K):
        if M & (1 << k):
            for i in range(N):
                B[i] = A[k][B[i]]

    for b in B:
        ans[b] += 1

    print(' '.join(map(str, ans)))
    return


if __name__ == '__main__':
    main()

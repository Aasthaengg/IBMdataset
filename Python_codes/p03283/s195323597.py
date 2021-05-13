def main():
    import sys
    input = sys.stdin.readline

    N, M, Q = map(int, input().split())

    tb = [[0] * (N + 1) for _ in range(N + 1)]
    # tb[L][R]:=区間LR内を走る列車総数
    for _ in range(M):
        L, R = map(int, input().split())
        tb[L][R] += 1

    for L in range(1, N + 1):
        for R in range(1, N + 1):
            tb[L][R] += tb[L - 1][R]
            tb[L][R] += tb[L][R - 1]
            tb[L][R] -= tb[L - 1][R - 1]

    ans = []
    for _ in range(Q):
        p, q = map(int, input().split())
        ans.append(tb[q][q] - tb[p - 1][q] - tb[q][p - 1] + tb[p - 1][p - 1])

    print(*ans, sep='\n')


if __name__ == '__main__':
    main()

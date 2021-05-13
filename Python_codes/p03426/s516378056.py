def main():
    import sys
    input = sys.stdin.readline

    H, W, D = map(int, input().split())
    A = [[int(x) for x in input().split()] for _ in range(H)]

    B = [0] * (H * W)

    C = [None] * (H * W)
    for r, row in enumerate(A):
        for c, cell in enumerate(row):
            C[cell - 1] = r, c

    for x in range(D, H * W):
        L, R = x - D, x
        lr, lc = C[L]
        rr, rc = C[R]
        B[R] = B[L] + abs(rr - lr) + abs(rc - lc)

    ans = []
    Q = int(input())
    for _ in range(Q):
        L, R = (int(x) - 1 for x in input().split())
        ans.append(B[R] - B[L])

    print(*ans, sep='\n')


if __name__ == '__main__':
    main()

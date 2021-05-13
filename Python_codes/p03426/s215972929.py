def main():
    import sys
    input = sys.stdin.readline

    H, W, D = map(int, input().split())
    A = [[int(x) for x in input().split()] for _ in range(H)]

    B = [[] for _ in range(D)]

    C = [None] * (H * W)
    for r, row in enumerate(A):
        for c, cell in enumerate(row):
            C[cell - 1] = r, c

    for x in range(H * W):
        r = x % D
        if B[r]:
            cr, cc = C[x]
            pr, pc = C[x - D]
            cost = abs(cr - pr) + abs(cc - pc)
            B[r].append(B[r][-1] + cost)

        else:
            B[r].append(0)

    ans = []
    Q = int(input())
    for _ in range(Q):
        L, R = (int(x) - 1 for x in input().split())
        r = R % D
        ql, qr = L // D, R // D

        ans.append(B[r][qr] - B[r][ql])

    print(*ans, sep='\n')


if __name__ == '__main__':
    main()

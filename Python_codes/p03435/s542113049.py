def main():
    G = [[int(x) for x in input().split()] for _ in range(3)]

    def is_ok(rs, cs):
        for r, ri in enumerate(rs, start=1):
            for c, ci in enumerate(cs):
                if G[r][c] != ri + ci:
                    return False
        return True

    for r0 in range(G[0][0] + 1):
        c0 = G[0][0] - r0
        c1 = G[0][1] - r0
        c2 = G[0][2] - r0

        r1 = G[1][0] - c0
        r2 = G[2][0] - c0

        rs = (r1, r2)
        cs = (c0, c1, c2)
        if is_ok(rs, cs):
            print('Yes')
            return

    print('No')


if __name__ == '__main__':
    main()

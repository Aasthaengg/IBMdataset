def main():
    import sys
    # readline = sys.stdin.readline
    readlines = sys.stdin.readlines
    H, W, N = map(int, input().split())
    grid = {}
    P = set()
    for s in readlines():
        a, b = map(int, s.split())
        a -= 1; b -= 1
        if a in grid:
            grid[a].add(b)
        else:
            grid[a] = set([b])
        P.add((a, b))

    ans = [0] * 10
    done = set()
    for a, b in P:
        for oa in range(a - 2, a + 1):
            for ob in range(b - 2, b + 1):
                if 0 <= oa <= H - 3 and 0 <= ob <= W - 3 and (oa, ob) not in done:
                    tmp = 0
                    for i in range(3):
                        for j in range(3):
                            na = oa + i
                            nb = ob + j
                            if (na, nb) in P:
                                tmp += 1
                    ans[tmp] += 1
                    done.add((oa, ob))
    
    ans[0] = (H - 2) * (W - 2) - sum(ans[1:])

    print(*ans, sep='\n')


if __name__ == "__main__":
    main()

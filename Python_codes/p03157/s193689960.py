def main():
    import sys
    sys.setrecursionlimit(10 ** 7)
    input = sys.stdin.readline

    h, w = map(int, input().split())
    s = [input().rstrip() for _ in range(h)]

    d = (1, 0), (-1, 0), (0, 1), (0, -1)

    checked = [[False] * w for _ in range(h)]

    def dfs(r, c):
        sharp, dot = 0, 0
        if s[r][c] == '#':
            sharp = 1
        else:
            dot = 1

        for dr, dc in d:
            nr = r + dr
            if nr < 0 or h <= nr:
                continue
            nc = c + dc
            if nc < 0 or w <= nc:
                continue
            if s[nr][nc] == s[r][c]:
                continue
            if checked[nr][nc]:
                continue
            checked[nr][nc] = True

            res_sharp, res_dot = dfs(nr, nc)
            sharp += res_sharp
            dot += res_dot

        return sharp, dot

    ret = 0
    for r in range(h):
        for c in range(w):
            if checked[r][c]:
                continue
            checked[r][c] = True
            sharp, dot = dfs(r, c)
            ret += sharp * dot

    print(ret)


if __name__ == '__main__':
    main()

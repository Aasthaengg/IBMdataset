def main():
    from functools import reduce
    from operator import mul
    import sys

    sys.setrecursionlimit(10 ** 7)

    def dfs(sr, sc):
        d = {'.': 0, '#': 0}
        q = [(sr, sc)]
        while q:
            r, c = q.pop()
            if checked[r][c]:
                continue
            checked[r][c] = True
            d[s[r][c]] += 1

            if r - 1 >= 0 and s[r - 1][c] != s[r][c]:
                q.append((r - 1, c))

            if c - 1 >= 0 and s[r][c - 1] != s[r][c]:
                q.append((r, c - 1))

            if r + 1 < h and s[r + 1][c] != s[r][c]:
                q.append((r + 1, c))

            if c + 1 < w and s[r][c + 1] != s[r][c]:
                q.append((r, c + 1))

        return d

    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]

    checked = [[False] * w for _ in range(h)]

    ret = 0
    for r in range(h):
        for c in range(w):
            if checked[r][c]:
                continue
            ret += reduce(mul, dfs(r, c).values())

    print(ret)


if __name__ == '__main__':
    main()

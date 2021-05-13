def main():
    import sys
    input = sys.stdin.readline

    H, W = map(int, input().split())
    s = [input().rstrip() for _ in range(H)]

    def wallen(g):
        L = len(g[0])
        ret = []
        ret.append('#' * (L + 2))
        for row in g:
            t = '#' + row + '#'
            ret.append(t)
        ret.append('#' * (L + 2))
        return ret

    g = wallen(s)
    # print(*g, sep='\n')

    left = [[-1] * (W + 2) for _ in range(H + 2)]  # 各方向に移動したときにぶつかる障害物の位置
    right = [[-1] * (W + 2) for _ in range(H + 2)]
    up = [[-1] * (W + 2) for _ in range(H + 2)]
    down = [[-1] * (W + 2) for _ in range(H + 2)]

    for r in range(H + 2):
        for c in range(W + 2):
            if g[r][c] == '#':
                left[r][c] = c
            else:
                left[r][c] = left[r][c - 1]

        for c in reversed(range(W + 2)):
            if g[r][c] == '#':
                right[r][c] = c
            else:
                right[r][c] = right[r][c + 1]

    for c in range(W + 2):
        for r in range(H + 2):
            if g[r][c] == '#':
                up[r][c] = r
            else:
                up[r][c] = up[r - 1][c]

        for r in reversed(range(H + 2)):
            if g[r][c] == '#':
                down[r][c] = r
            else:
                down[r][c] = down[r + 1][c]

    ans = 0
    for r in range(H + 2):
        for c in range(1, W + 1):
            t = right[r][c] - left[r][c] + down[r][c] - up[r][c] - 3
            ans = max(ans, t)

    print(ans)


if __name__ == '__main__':
    main()

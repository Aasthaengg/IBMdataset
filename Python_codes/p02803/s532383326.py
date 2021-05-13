def main():
    import sys
    readline = sys.stdin.buffer.readline

    from collections import deque

    h, w = map(int, readline().split())
    s = ['#'*(w+2)] + ['#' + readline().rstrip().decode('utf-8') + '#' for _ in range(h)] + ['#'*(w+2)]

    l = []
    for i in range(h+2):
        for j in range(w+2):
            if s[i][j] == '.':
                l.append((i, j))
    dire = ((0, 1), (0, -1), (1, 0), (-1, 0))
    q = deque()
    ans = 0
    for hh, ww in l:
        q.appendleft((hh, ww, 0))
        c = [[0]*(w+2) for _ in range(h+2)]
        while q:
            ha, wa, ca = q.pop()
            if c[ha][wa] == 0:
                c[ha][wa] = 1
                ans = max(ans, ca)
                for dh, dw in dire:
                    hdh, wdw = ha+dh, wa+dw
                    if s[hdh][wdw] == '.' and c[hdh][wdw] == 0:
                        q.appendleft((hdh, wdw, ca+1))
    print(ans)

main()
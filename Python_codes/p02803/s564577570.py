def main():
    import sys
    readline = sys.stdin.buffer.readline

    from collections import deque

    h, w = map(int, readline().split())
    s = [readline().rstrip().decode('utf-8') for _ in range(h)]

    l = []
    for i in range(h):
        for j in range(w):
            if s[i][j] == '.':
                l.append((i, j))
    dire = ((0, 1), (0, -1), (1, 0), (-1, 0))
    q = deque()
    ans = 0
    for hh, ww in l:
        q.appendleft((hh, ww, 0))
        c = [[0]*w for _ in range(h)]
        while q:
            ha, wa, ca = q.pop()
            if c[ha][wa] == 0:
                c[ha][wa] = 1
                ans = max(ans, ca)
                for dh, dw in dire:
                    hdh, wdw = ha+dh, wa+dw
                    if 0 <= hdh < h and 0 <= wdw < w:
                        if s[hdh][wdw] == '.' and c[hdh][wdw] == 0:
                            q.appendleft((hdh, wdw, ca+1))
    print(ans)

main()
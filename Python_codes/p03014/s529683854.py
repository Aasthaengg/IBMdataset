h,w = list(map(int, input().split()))
b = [input() + '#' for _ in range(h)]
b.append('#' * (w + 1))
ans = [[0]*w for _ in range(h)]

for r in range(h):
    c = 0
    while c < w:
        if b[r][c] == '#':
            c += 1
        else:
            st = c
            while b[r][c] == '.':
                c += 1
            for i in range(st, c):
                ans[r][i] += (c - st)

for c in range(w):
    r = 0
    while r < h:
        if b[r][c] == '#':
            r += 1
        else:
            st = r
            while b[r][c] == '.':
                r += 1
            for i in range(st, r):
                ans[i][c] += (r - st)

import itertools
print(max(itertools.chain.from_iterable(ans))-1)

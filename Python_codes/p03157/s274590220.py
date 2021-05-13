# https://atcoder.jp/contests/aising2019/tasks/aising2019_c

import sys
sys.setrecursionlimit(10 ** 7)

H, W = map(int, input().split())
M = [list(input()) for _ in range(H)]
seen = [[False for _ in range(W)] for _ in range(H)]


def dfs(h, w, ph, pw):
    if M[h][w] == '.':
        bc, wc = 0, 1
    else:
        bc, wc = 1, 0
    for (dh, dw) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nh, nw = h + dh, w + dw
        if nh < 0 or H <= nh or nw < 0 or W <= nw:
            continue
        if nh == ph and nw == pw:
            continue
        if seen[nh][nw]:
            continue
        if M[nh][nw] == M[h][w]:
            continue
        seen[nh][nw] = True
        b_add, w_add = dfs(nh, nw, h, w)
        bc += b_add
        wc += w_add
    return bc, wc

ans = 0
for h in range(H):
    for w in range(W):
        if seen[h][w] == False:
            seen[h][w] = True
            b, w = dfs(h, w, -1, -1)
            ans += b * w
print(ans)
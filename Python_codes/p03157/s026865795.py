import sys
sys.setrecursionlimit(10 ** 7)
h, w = map(int, input().split())
s = [input() for _ in range(h)]
seen = [[False for _ in range(w)] for _ in range(h)]

def dfs(bx, by, sx, sy):
    if s[sx][sy] == '.':
        b_cnt, w_cnt = 0, 1
    else:
        b_cnt, w_cnt = 1, 0
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        px, py = sx + dx, sy + dy
        #print('=', px, py)
        if bx == px and by == py:
            #print(px, py, 'flg1')
            continue
        if px < 0 or h <= px or py < 0 or w <= py:
            #print(px, py, 'flg2')
            continue
        if seen[px][py]:
            #print(px, py, 'flg3')
            continue
        if s[sx][sy] == s[px][py]:
            #print(px, py, 'flg4')
            continue
        seen[px][py] = True
        b_add, w_add = dfs(sx, sy, px, py)
        b_cnt += b_add
        w_cnt += w_add

    return b_cnt, w_cnt

ans = 0
#print(dfs(-1, -1, 1, 1))
for i in range(h):
    for j in range(w):
        if seen[i][j] == False:
            seen[i][j] = True
            b_cnt, w_cnt = dfs(-1, -1, i, j)
            ans += b_cnt * w_cnt

print(ans)
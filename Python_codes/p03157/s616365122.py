import sys
sys.setrecursionlimit(10**8)
h, w = [int(i) for i in sys.stdin.readline().split()]
s_ls = []
bl_ls = []
for i in range(h):
    s = [1 if i == "#" else -1 for i in sys.stdin.readline().strip()]
    for j, k in enumerate(s):
        if k == 1:
            bl_ls.append((i, j))
    s_ls.append(s)

memo_ls = dict()
def dfs(y, x, col):
    if (y, x) in memo_ls:
        return memo_ls[(y, x)]
    res = 0
    if col == -1:
        res += 1
    already.add((y, x))
    for move_y, move_x in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        next_y = y + move_y
        next_x = x + move_x
        if 0 <= next_x < w and 0 <= next_y < h and s_ls[next_y][next_x] == (-1) * col and (next_y, next_x) not in already:
            res += dfs(next_y, next_x, (-1) * col)
    return res

ans = 0
for bl in bl_ls:
    already = set()
    stack = [(bl[0], bl[1], 1, 0)]
    cnt = 0
    while len(stack) > 0:
        y, x, col, _sum = stack.pop(-1)
        if (y, x) in memo_ls:
            cnt = memo_ls[(y, x)]
            break
        if col == -1:
            cnt += 1
        already.add((y, x))
        for move_y, move_x in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_y = y + move_y
            next_x = x + move_x
            if 0 <= next_x < w and 0 <= next_y < h and s_ls[next_y][next_x] == (-1) * col and (
            next_y, next_x) not in already:
                stack.append((next_y, next_x, (-1) * col, _sum))
                already.add((next_y, next_x))
    res = cnt
    ans += res
    for al in list(already):
        memo_ls[al] = res
print(ans)